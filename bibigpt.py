import requests
import json
import re
import plugins  # 导入自定义的插件模块
from bridge.reply import Reply, ReplyType
from plugins import *
from config import conf

@plugins.register(
    name="bibigpt",
    desire_priority=2,
    hidden=False,
    desc="A plugin for summarizing videos",
    version="0.0.1",
    author="fatwang2",
)
class bibigpt(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
        print("[bibigpt] inited")

    def on_handle_context(self, e_context: EventContext):
        content = e_context["context"].content
        
        # Check if the content is a URL
        if re.match('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', content):
            
            headers = {
                'Content-Type': 'application/json',
            }
            payload = json.dumps({
                "url": content,
                "includeDetail": False
            })            
            video_key = conf().get("video_key")  # 获取配置文件中的video_key

            try:
                api_url = f"https://bibigpt.co/api/open/{video_key}"
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
