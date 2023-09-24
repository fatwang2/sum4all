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
    version="0.0.3",
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
            self.get_summary_from_url(content, e_context)
            return
        # 检查是否为 HTTP URL
        if re.match('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', content):
            self.get_summary_from_url(content, e_context)
            return
    def get_summary_from_url(self, url: str, e_context: EventContext):    
            headers = {
                'Content-Type': 'application/json',
            }
            payload = json.dumps({
                "url": url,
                "includeDetail": False
            })            
            try:
                api_url = f"https://bibigpt.co/api/open/{self.sum_key}"
                response = requests.request("POST",api_url, headers=headers, data=payload)
                response.raise_for_status()
                data = json.loads(response.text)
                summary = data.get('summary', 'Summary not available')
                html_url = data.get('htmlUrl', 'HTML URL not available')
               

            except requests.exceptions.RequestException as e:
                summary = f"An error occurred: {e}"

            reply = Reply()
            reply.type = ReplyType.TEXT
            reply.content = ""
            reply.content = f"{summary}\n\n详情：{html_url}"

            e_context["reply"] = reply
            e_context.action = EventAction.BREAK_PASS

    def get_help_text(self, **kwargs):
        help_text = "输入url，直接为你总结，包括视频、文章等\n"
        return help_text
