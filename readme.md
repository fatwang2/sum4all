## 更新日志
- V0.0.6，20230925，支持用户配置自己的短链接服务token，新增短链接生成失败时的兜底机制
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

## 申请
通过链接注册bibigpt服务 [注册地址](https://bibigpt.co/r/90nEPW)，获取总结key，注册免费享有60min时长，请注意，只有 https://bibigpt.co/api/open/ 后面的部分是key

![Alt text](picture/image-3.png)

## 配置
服务器部署：复制插件目录的`config.json.template`文件,重命名为`config.json`，在`sum_key`字段填入申请的key

docker部署：参考项目docker部署的插件使用，`config.json`配置文件内增加sum4all插件的配置参数

## 后续计划
- 支持切换不同的总结服务
- 支持企业微信的链接卡片
- 支持配置总结的prompt
- 支持输出总结图片
- 支持文章对话
- 支持文件总结与对话
- 支持视频号