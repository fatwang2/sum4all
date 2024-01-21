## 用户交流
[telegram频道 ](https://sum4all.site/telegram)

## 更新日志
- V0.6.8，20230121，增加对不支持文件类型忽略的逻辑；更换底层搜索、内容获取服务，更快更稳定；更新配置文件里的搜索默认prompt
- V0.6.7，20230109，增加讯飞代理，简化讯飞部分代码与依赖
- V0.6.6，20230106，增加Gemini代理，解决非美国IP无法访问Gemini的问题
- V0.6.5，20231217，结构化配置文件config.json，支持更灵活的调整文件、图片、URL、搜索的配置，升级后需按照新格式配置
- V0.6.4，20231216，文件、图像总结支持Google最新的Gemini模型
- V0.6.2，20231216，链接、搜索总结支持Google最新的Gemini模型，目前免费
- V0.6.1，20231215，修复搜索bug
- V0.6.1，20231214，企业微信ntwork模式，支持链接卡片、文件、图片，注意需更新chatgpt-on-wechat到最新版
- V0.6.0，20231210，支持文件、链接多轮对话，OpenAI支持搜索模式
- V0.5.6，20231209，支持搜索提示词的自定义配置
- V0.5.5，20231209，支持图片多轮对话，图片默认总结后，5min内输入提问提示词即可继续追问，提示词可自定义
- V0.5.1，20231209，群聊开关支持图片、文件，可通过修改配置文件的group_sharing来判断是否支持自动对群聊的图片、文件做总结
- V0.5.0，20231206，新增支持讯飞图片总结功能，免费赠送200万token，感谢alexgang的PR

[更多日志](https://github.com/fatwang2/sum4all/releases)

## 简介
本项目为微信插件，需配合[chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)项目使用

## 功能特点
- 支持联网搜索
- 支持多轮追问
- 支持文章内容总结，个人微信支持链接卡片和url，企微支持url
- 支持文件内容总结，包括pdf、doc、markdown、txt、xls、csv、html、ppt
- 支持图片总结，包括png、jpeg、jpg
- 支持视频、播客内容总结，包括抖音、b站、小红书、YouTube等
- 支持多种内容总结服务，可自由组合
- 支持自定义prompt
- 支持自定义搜索、追问提示词
<table>
  <tr>
    <td><img src="picture/追问.png" width="400px" alt="文件" /></td>
    <td><img src="picture/WX20231202-183138@2x.png" width="400px" alt="搜索" /></td>
  </tr>
  <tr>
    <td><img src="picture/WX20231203-021149@2x.png" width="400px" alt="图片" /></td>  
    <td><img src="picture/image-6.png" width="400px" alt="链接卡片" /></td>

  </tr>
  <tr>
    <td><img src="picture/抖音.png" width="400px" alt="抖音" /></td>    
    <td><img src="picture/image.png" width="400px" alt="小红书" /></td> 
  </tr>
  
</table>

## 安装
使用管理员口令在线安装，管理员认证方法见：[管理员认证](https://github.com/zhayujie/chatgpt-on-wechat/tree/master/plugins/godcmd)
```
#installp https://github.com/fatwang2/sum4all.git
```
安装成功后，根据提示使用`#scanp` 命令来扫描新插件

![Alt text](picture/image-4.png)

## 申请服务（自行选择，各有优劣）

| 服务 | 支持功能 | 特点 | 注册地址 | 图片介绍 |
|------|----------|------|----------|-----------|
| OpenAI | 搜索、文件、图片、绝大部分网页文章 | 无需额外申请服务，舍得花钱的话，效果最可控 | [OpenAI](https://platform.openai.com/account/api-keys) \| [LinkAI代理](https://sum4all.site/linkai) | ![OpenAI](picture/openai.png) |
| Sum4all | 搜索、文件、绝大部分网页文章 | 注册免费送1万token，邀请好友注册再各得5k，觉得好用的还可以注册Poe上的同名机器人 | [sum4all](https://sum4all.site/key) \| [Poe Sum4all机器人](https://sum4all.site/poe) | ![Sum4all](picture/sum4all.png) |
| Gemini | 搜索、文件、图片、绝大部分网页文章 | Google最新大模型，免费 | [gemini](https://sum4all.site/google) | ![Gemini](picture/gemini.png) |
| Perplexity | 搜索 | 国外的搜索总结服务，速度快，价格贵，自带大模型，需自行注册和付费 | [Perplexity](https://sum4all.site/perplexity) | ![Perplexity](picture/p.png) | ![Alt text](picture/WX20231201-004639@2x.png) |
| 讯飞 | 图片 | 讯飞星火大模型的图片理解功能，免费200万token，随便用 | [xunfei](https://sum4all.site/xunfei) | ![Perplexity](picture/讯飞.png) |
| BibiGPT | 文章、视频、音频 | 注册免费享有60min时长 | [BibiGPT](https://sum4all.site/bibigpt) | ![BibiGPT](picture/image-3.png) |
| OpenSum | 微信、头条、即刻等平台网页文章 | 19元30万字 | [OpenSum](https://sum4all.site/opensum) | ![OpenSum](picture/opensum.png) |


## 配置
- 服务器部署：复制插件目录的`config.json.template`文件,重命名为`config.json`，配置参数即可
- docker部署：参考项目docker部署的插件使用，`config.json`内增加sum4all插件的配置参数，操作见 [docker插件配置](https://github.com/zhayujie/chatgpt-on-wechat#3-%E6%8F%92%E4%BB%B6%E4%BD%BF%E7%94%A8)

配置文件含义如下：
```
{
  "url_sum": {
    "enabled": true, #url总结服务开关
    "service": "sum4all", #url总结服务，目前支持openai、sum4all、gemini、bibigpt、opensum
    "group": true, #url总结群聊开关
    "qa_prefix":"问", #ulr总结追问前缀词
    "prompt": "" #ulr总结prompt
  },
  "search_sum": {
    "enabled": false, #搜索总结服务开关
    "service": "sum4all", #搜索总结服务，目前支持openai、sum4all、gemini、perplexity
    "group": true, #搜索总结群聊开关
    "search_prefix":"搜", #搜索总结前缀词
    "prompt": "" #搜索总结prompt
  },
  "file_sum": {
    "enabled": false, #文件总结服务开关
    "service": "sum4all", #文件总结服务，目前支持openai、sum4all、gemini
    "group": true, #文件总结群聊开关
    "qa_prefix":"问", #文件总结追问前缀词
    "prompt": "" #文件总结prompt
  },
  "image_sum": {
    "enabled": false, #图片总结服务开关
    "service": "gemini", #图片总结服务，目前支持openai、gemini、xunfei
    "group": true, #图片总结群聊开关
    "qa_prefix":"问", #图片总结追问前缀词
    "prompt": "" #图片总结prompt
  },
  "keys": {
    "sum4all_key": "", #如选sum4all，则必填
    "gemini_key": "", #如选gemini，则必填
    "perplexity_key": "", #如选perplexity，则必填
    "open_ai_api_key": "", #如选openai，则必填
    "model": "gpt-3.5-turbo", #openai模型
    "open_ai_api_base": "https://api.openai.com/v1", #openai请求地址
    "xunfei_app_id": "", #讯飞大模型appid，如选xunfei，则必填
    "xunfei_api_key": "", #讯飞大模型apikey，如选xunfei，则必填
    "xunfei_api_secret": "", #讯飞大模型apisecret，如选xunfei，则必填
    "opensum_key": "", #如选opensum，则必填
    "bibigpt_key": "", #如选bibigpt，则必填
    "outputLanguage": "zh-CN" #bibigpt的输出语言，默认中文，其他支持列表见下
  }
}
```
bibigpt输出语言支持列表：
```
  English: 'en-US',
  中文: 'zh-CN',
  繁體中文: 'zh-TW',
  日本語: 'ja-JP',
  Italiano: 'it-IT',
  Deutsch: 'de-DE',
  Español: 'es-ES',
  Français: 'fr-FR',
  Nederlands: 'nl-NL',
  한국어: 'ko-KR',
  ភាសាខ្មែរ: 'km-KH',
  हिंदी: 'hi-IN',
```

## 后续计划
- 支持输出总结图片
- 支持视频号总结
- 支持通过管理员指令切换内容总结服务、配置参数等

## 赞助地址
如果有幸帮到你，请随意打赏

![Alt text](picture/微信.jpg)

## 赞助名单
- 兔子橙