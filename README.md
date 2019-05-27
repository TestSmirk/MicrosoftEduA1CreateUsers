# MicrosoftEduA1CreateUsers
### 批量创建微软教育A1用户
* 下载代码到你的任意目录下
`pip install requests`  python2  


* 首先打开F12 我一般是`ctri + shift+c` 打开的 选中 network  

![https://github.com/TestSmirk/MicrosoftEduA1CreateUsers/blob/master/img/001.png](https://github.com/TestSmirk/MicrosoftEduA1CreateUsers/blob/master/img/001.png)

* 然后创建一个用户用户名 默认`mjj002`  

![](https://github.com/TestSmirk/MicrosoftEduA1CreateUsers/blob/master/img/002.png)

* 然后选中user这个选项  

![](https://github.com/TestSmirk/MicrosoftEduA1CreateUsers/blob/master/img/003.png)

* 找到 Request Headers的`ajaxsessionkey`,`cookie` 两个字段 然后分别扔到对应的文件里.

![](https://github.com/TestSmirk/MicrosoftEduA1CreateUsers/blob/master/img/004.png)

* 找到 Requyest Payload 点击viewsource  复制整个json(很长)到`payload.json`文件里
![](https://github.com/TestSmirk/MicrosoftEduA1CreateUsers/blob/master/img/005.png)


* 如果创建的用户名不是mjj002 需要修改 CreateUser.py的第7行 `FITST_USER_NAME` 为刚刚创建的用户名. 

运行 `python CreateUser.py `


默认是从 0000001 开始创建 下一个用户名字是上一个用户的密码.
