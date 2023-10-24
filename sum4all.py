import requests
import json
import re
import plugins  # 导入自定义的插件模块
from bridge.reply import Reply, ReplyType
from bridge.context import ContextType
from bridge import bridge
from plugins import *
from config import conf
from common.log import logger
import os

@plugins.register(
    name="sum4all",
    desire_priority=2,
    hidden=False,
    desc="A plugin for summarizing videos and articels",
    version="0.1.0",
    author="fatwang2",
)
class sum4all(Plugin):
    def __init__(self):
        super().__init__()
        try:
        # 读取配置文件
            config_path = os.path.join(os.path.dirname(__file__), "config.json")
            with open(config_path, "r", encoding="utf-8") as f:
                conf = json.load(f)
        
        # 从配置中取得 sum_key
            self.sum_key = conf["sum4all"]["sum_key"]
            self.outputLanguage = conf["sum4all"].get("outputLanguage", "zh-CN")
            self.group_sharing = conf["sum4all"].get("group_sharing", True)

        # 设置事件处理函数
            self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
        
        # 初始化成功日志
            logger.info("sum4all inited.")
        
        except Exception as e:
        # 初始化失败日志
            logger.warn("sum4all init failed.")
        # 抛出异常
            raise e

    def on_handle_context(self, e_context: EventContext):
        context = e_context["context"]
        if context.type not in [ContextType.TEXT, ContextType.SHARING]:  # filter content no need solve
            return
        content = context.content
        isgroup = e_context["context"].get("isgroup", False)
        url_match = re.match('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', content)
        unsupported_urls = re.search(r'.*finder\.video\.qq\.com.*|.*support\.weixin\.qq\.com/update.*|.*support\.weixin\.qq\.com/security.*|.*mp\.weixin\.qq\.com/mp/waerrpage.*', content)
        if context.type == ContextType.SHARING:  #匹配卡片分享
            if unsupported_urls:  #匹配不支持总结的卡片
                if isgroup:  ##群聊中忽略
                    return
                else:  ##私聊回复不支持
                    logger.info("[sum4all] Unsupported URL : %s", content)
                    reply = Reply(type=ReplyType.TEXT, content="不支持总结小程序和视频号")
                    e_context["reply"] = reply
                    e_context.action = EventAction.BREAK_PASS
            else:  #匹配支持总结的卡片
                if isgroup:  #处理群聊总结
                    if self.group_sharing:  #group_sharing = True进行总结，False则忽略。
                        logger.info("[sum4all] Summary URL : %s", content)
                        self.get_summary_from_url(content, e_context)
                        return
                    else:
                        return
                else:  #处理私聊总结
                    logger.info("[sum4all] Summary URL : %s", content)
                    self.get_summary_from_url(content, e_context)
                    return
        elif url_match: #匹配URL链接
            if unsupported_urls:  #匹配不支持总结的网址
                logger.info("[sum4all] Unsupported URL : %s", content)
                reply = Reply(type=ReplyType.TEXT, content="不支持总结小程序和视频号")
                e_context["reply"] = reply
                e_context.action = EventAction.BREAK_PASS
            else:
                logger.info("[sum4all] Summary URL : %s", content)
                self.get_summary_from_url(content, e_context)
                return
    
    def get_short_url(self, long_url):
        url = "https://s.fatwang2.com"
        payload = {
            "url": long_url
        }        
        headers = {'Content-Type': "application/json"}
        response = requests.request("POST", url, json=payload, headers=headers)
        if response.status_code == 200:
            res_data = response.json()
            if res_data.get('status') == 200:
                short_key = res_data.get('key', None)  # 获取 'key' 字段的值
        
                if short_key:
                    # 拼接成完整的短链接
                    return f"https://s.fatwang2.com{short_key}"
        return None

    def get_summary_from_url(self, url: str, e_context: EventContext):    
            headers = {
                'Content-Type': 'application/json',
            }
            payload_params = {
                "url": url,
                "includeDetail": False,
                "promptConfig": {
                    "outputLanguage": self.outputLanguage
                }
            }
    
            payload = json.dumps(payload_params)           
            try:
                api_url = f"https://bibigpt.co/api/open/{self.sum_key}"
                response = requests.request("POST",api_url, headers=headers, data=payload)
                response.raise_for_status()
                data = json.loads(response.text)
                summary_original = data.get('summary', 'Summary not available')
                html_url = data.get('htmlUrl', 'HTML URL not available')
                # 获取短链接
                short_url = self.get_short_url(html_url) 
                
                # 如果获取短链接失败，使用 html_url
                if short_url is None:
                    short_url = html_url if html_url != 'HTML URL not available' else 'URL not available'
                
                # 移除 "##摘要"、"## 亮点" 和 "-"
                summary = summary_original.split("详细版（支持对话追问）")[0].replace("## 摘要\n", "").replace("## 亮点\n", "").replace("- ", "")
            except requests.exceptions.RequestException as e:
                summary = f"An error occurred: {e}"

            reply = Reply()
            reply.type = ReplyType.TEXT
            reply.content = ""
            reply.content = f"{summary}\n\n详细链接：{short_url}"

            e_context["reply"] = reply
            e_context.action = EventAction.BREAK_PASS

    def get_help_text(self, **kwargs):
        help_text = "输入url，直接为你总结，包括视频、文章等\n"
        return help_text
