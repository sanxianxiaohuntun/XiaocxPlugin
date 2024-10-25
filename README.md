# XiaocxPlugin

## 安装
配置完成 [QChatGPT](https://github.com/RockChinQ/QChatGPT) 主程序后使用管理员账号向机器人发送命令即可安装：<br />

```
!plugin get https://github.com/sanxianxiaohuntun/XiaocxPlugin.git
```
或查看详细的[插件安装说明](https://github.com/RockChinQ/QChatGPT/wiki/5-%E6%8F%92%E4%BB%B6%E4%BD%BF%E7%94%A8)

## 使用

&nbsp;
这只是一个加载程序内部包含一些案例，可以让用户自主添加小程序，比如/天气 /色图 /今日运势 之类的各种小功能<br />
&nbsp;
小程序开发及其简单，把你需要的功能告诉gpt然后把我的案例程序代码给GPT，GPT生成后丢到data目录下即可，目前还在更新测试<br />
&nbsp;
## 使用方法：
1.用GPT或者自己写又或者下载的py小程序（只支持图片和文本类）<br />
&nbsp;<br />
2.放到QChatGPT\plugins\XiaocxPlugin\data<br />
&nbsp;<br />
3.使用/命令启用小插件（放进去后无需重启主程序）比如你放入了文件叫做"色图.py"，你就使用"/色图"命令即可使用，如果要增加小程序安装data目录下文件逻辑写即可<br />
&nbsp;<br />
4.文件类型（一律参考data目录下文件） /命令 xxxx类型文件可参考"天气.py"，图片类型参考"色图.py"<br />
&nbsp;<br />
5./命令如果冲突可以修改QChatGPT\plugins\XiaocxPlugin目录下main.py的"if cleaned_text.startswith('/'):"位置"/"修改为你想要的即可比如：/改为AAA，"if cleaned_text.startswith('AAA')"<br />
&nbsp;<br />
&nbsp;<br />
## 位置图
![before](https://raw.githubusercontent.com/sanxianxiaohuntun/wodecuntu12/refs/heads/main/%E4%BD%8D%E7%BD%AE.png)
&nbsp;<br />
&nbsp;<br />
&nbsp;<br />
## 插件图
![before](https://raw.githubusercontent.com/sanxianxiaohuntun/wodecuntu12/refs/heads/main/%E8%89%B2%E5%9B%BE.png)
![before](https://raw.githubusercontent.com/sanxianxiaohuntun/wodecuntu12/refs/heads/main/%E5%A4%A9%E6%B0%94.png)
![before](https://raw.githubusercontent.com/sanxianxiaohuntun/wodecuntu12/refs/heads/main/%E5%A4%9A%E4%B8%AA.png)

## 小白专用GPT自制插件生成教程

![before](https://raw.githubusercontent.com/sanxianxiaohuntun/wodecuntu12/refs/heads/main/%E6%95%99%E5%AD%A6.jpg)
