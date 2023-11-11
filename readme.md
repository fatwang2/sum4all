## 更新日志
- V0.1.3，20231112，新增支持OpenAI、OpenSum两种总结服务，通过配置文件可切换；支持Docker部署
- V0.1.0，20231025，去除重复短链接
- V0.0.9，20231002，新增group_sharing参数，设为false时，群聊不自动总结卡片链接。新增对不支持链接的回复提示。
- V0.0.8，20230927，屏蔽小程序与视频号链接，暂时不支持
- V0.0.7，20230926，去除短链接服务key的配置，自建短链接服务开放使用，无需单独申请
- V0.0.6，20230925，支持用户配置自己的短链接服务key，新增短链接生成失败时的兜底机制
- V0.0.5，20230925，支持配置语言参数，变量在config.json中，默认中文
- V0.0.4，20230925，详情长链接转换成短链接，去除原有markdown格式标记，内容更简洁
- V0.0.3，20230924，支持微信文章链接卡片识别，chatgpt-on-wechat需更新到最新代码
- V0.0.2，20230924，插件更名，支持插件目录内的配置文件。**由于更名，旧插件需卸载后重装**
- V0.0.1，20230910，发布视频、文章总结插件

## 简介
本项目为微信插件，需配合[chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)项目使用，可以对文章、视频、播客内容做总结，覆盖b站、抖音、快手、小红书、微信等各个平台！具体效果如下
![链接卡片](picture/image-6.png)
![小红书](picture/image.png)
![抖音](picture/%E6%8A%96%E9%9F%B3.png)

## 安装
使用管理员口令在线安装，管理员认证方法见：[管理员认证](https://github.com/zhayujie/chatgpt-on-wechat/tree/master/plugins/godcmd)
```
#installp https://github.com/fatwang2/sum4all.git
```
安装成功后，根据提示使用`#scanp` 命令来扫描新插件

![Alt text](picture/image-4.png)

## 申请服务（三选一即可，推荐OpenAI）
OpenAI（大部分文章）：有OpenAI API权限即可

OpenSum（部分文章）：通过链接注册 [注册地址](https://open.chatsum.ai/#/guide/apply?id=%e7%94%b3%e8%af%b7-api_key)，获取总结key，19元30万字

BibiGPT（文章、视频、音频）：通过链接注册 [注册地址](https://bibigpt.co/r/tfcGVE)，获取总结key，注册免费享有60min时长，请注意，只有 `https://bibigpt.co/api/open/` 后面的部分是key

![Alt text](picture/image-3.png)
## 配置
- 服务器部署：复制插件目录的`config.json.template`文件,重命名为`config.json`，配置参数即可
- docker部署：参考项目docker部署的插件使用，`config.json`内增加sum4all插件的配置参数，操作见 [docker插件配置](https://github.com/zhayujie/chatgpt-on-wechat#3-%E6%8F%92%E4%BB%B6%E4%BD%BF%E7%94%A8)

各参数含义如下：
```
"sum_service":"", #内容总结服务，openai、bibigpt、opensum
"group_sharing": true, #是否支持群聊内的链接卡片
"opensum_key": "", #如选opensum，则必填
"open_ai_api_key": "", #如选openai，则必填
"model": "gpt-3.5-turbo-1106", #openai模型
"open_ai_api_base": "https://api.openai.com/v1", #openai请求地址
"prompt": "你是一个新闻专家，我会给你发一些网页内容，请你用简单明了的语言做总结。第一部分是「📌总结」，一句话讲清楚整篇文章的核心观点，控制在50字左右，第二部分是「💡要点」，用数字序号列出来3-5个文章的核心内容。如果需要可以使用emoji让你的表达更生动" #openai内容总结prompt
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
- 支持企业微信的链接卡片
- 支持输出总结图片
- 支持文章对话
- 支持文件总结与对话
- 支持视频号
