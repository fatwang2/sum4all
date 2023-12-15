## 用户交流
[telegram频道 ](https://t.me/+w2Z8S0Y8H2IxZDI9)

## 更新日志
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
| Perplexity | 搜索 | 国外的搜索总结服务，速度快，价格贵，自带大模型，需自行注册和付费 | [Perplexity](https://sum4all.site/perplexity) | ![Perplexity](picture/p.png) | ![Alt text](picture/WX20231201-004639@2x.png) |
| 讯飞 | 图片 | 讯飞星火大模型的图片理解功能，免费200万token，随便用 | [xunfei](https://sum4all.site/xunfei) | ![Perplexity](picture/讯飞.png) |
| BibiGPT | 文章、视频、音频 | 注册免费享有60min时长 | [BibiGPT](https://sum4all.site/bibigpt) | ![BibiGPT](picture/image-3.png) |
| OpenSum | 微信、头条、即刻等平台网页文章 | 19元30万字 | [OpenSum](https://sum4all.site/opensum) | ![OpenSum](picture/opensum.png) |


## 配置
- 服务器部署：复制插件目录的`config.json.template`文件,重命名为`config.json`，配置参数即可
- docker部署：参考项目docker部署的插件使用，`config.json`内增加sum4all插件的配置参数，操作见 [docker插件配置](https://github.com/zhayujie/chatgpt-on-wechat#3-%E6%8F%92%E4%BB%B6%E4%BD%BF%E7%94%A8)

各参数含义如下：
```
"sum_service":"", #内容总结服务，openai、sum4all、bibigpt、opensum
"search_sum":"", #搜索开关，默认不开启，开启需改为 true，在微信端使用时，需要以“搜”字开头才会触发
"file_sum": false, #文件总结开关，默认不开启，开启需改为 true，目前支持sum_service为openai和sum4all
"image_sum": false, #图片总结开关，默认不开启，开启需改为 true，目前支持sum_service为openai和xunfei
"search_service":"", #搜索服务，目前支持sum_service为sum4all、openai和perplexity
"image_service":"", #图片总结服务，目前支持openai和xunfei
"group_sharing": true, #是否支持群聊内的链接卡片、文件和图片
"qa_prefix":"问", #追问提示词，以该词开头，才能触发追问
"search_prefix":"搜", #搜索提示词，以该词开头，才能触发搜索
"sum4all_key":"", #如选sum4all，则必填
"xunfei_app_id": "", #讯飞大模型appid，如图片总结服务选择xunfei，则必填
"xunfei_api_key": "", #讯飞大模型apikey，如图片总结服务选择xunfei，则必填
"xunfei_api_secret": "" #讯飞大模型apisecret，如图片总结服务选择xunfei，则必填
"opensum_key": "", #如选opensum，则必填
"open_ai_api_key": "", #如选openai，则必填
"perplexity_key":"", #如搜索服务选perplexity，则必填
"model": "gpt-3.5-turbo-1106", #openai模型
"open_ai_api_base": "https://api.openai.com/v1", #openai请求地址
"prompt": "你是一个新闻专家，我会给你发一些网页内容，请你用简单明了的语言做总结。第一部分是「📌总结」，一句话讲清楚整篇文章的核心观点，控制在50字左右，第二部分是「💡要点」，用数字序号列出来3-5个文章的核心内容。如果需要可以使用emoji让你的表达更生动" #openai内容总结prompt
"search_prompt":"你是一个信息检索专家，请你用简单明了的语言，对你收到的内容做总结。尽量使用emoji让你的表达更生动" #搜索总结prompt
"bibigpt_key": "", #如选bibigpt，则必填
"outputLanguage": "zh-CN",#bibigpt的输出语言，默认中文，其他支持列表见下
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
- 结构化配置文件
- 支持输出总结图片
- 支持视频号总结
- 支持通过管理员指令切换内容总结服务、配置参数等

## 赞助地址
![Alt text](picture/usdt.png)