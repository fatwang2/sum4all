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
    version="0.0.5",
    author="fatwang2",
)
class sum4all(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
        try:
        # 读取配置文件
            config_path = os.path.join(os.path.dirname(__file__), "config.json")
            with open(config_path, "r", encoding="utf-8") as f:
                conf = json.load(f)
        
        # 从配置中取得 sum_key
            self.sum_key = conf["sum4all"]["sum_key"]
            self.outputLanguage = conf["sum4all"].get("outputLanguage", "zh-CN")

        
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
        content = context.content        
        # 检查是否为 SHARING 类型的消息
        if context.type == ContextType.SHARING:
            # 获取sharing信息
            self.get_summary_from_url(content, e_context)
            return
        # 检查是否为 HTTP URL
        if re.match('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', content):
            self.get_summary_from_url(content, e_context)
            return
    def get_short_url(self, long_url, token):
        url = "https://v2.alapi.cn/api/url"
        payload = f"token={token}&url={long_url}&type=dwz"
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers)
        if response.status_code == 200:
            res_data = response.json()
            if res_data.get('code') == 200:
                return res_data['data']['short_url']
        return None

    def get_summary_from_url(self, url: str, e_context: EventContext):    
            headers = {
                'Content-Type': 'application/json',
            }
            payload = json.dumps({
                "url": url,
                "includeDetail": False
                "promptConfig": {
                    "outputLanguage": self.outputLanguage
                }
            })            
            try:
                api_url = f"https://bibigpt.co/api/open/{self.sum_key}"
                response = requests.request("POST",api_url, headers=headers, data=payload)
                response.raise_for_status()
                data = json.loads(response.text)
                summary_original = data.get('summary', 'Summary not available')
                long_url = data.get('htmlUrl', 'HTML URL not available')
                # 获取短链接
                token = "Wurd4RSCVSpbCpFd" 
                short_url = self.get_short_url(long_url, token) if long_url != 'HTML URL not available' else 'Short URL not available'
                # 移除 "##摘要"、"## 亮点" 和 "-"
                summary = summary_original.replace("## 摘要\n", "").replace("## 亮点\n", "").replace("- ", "")
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
