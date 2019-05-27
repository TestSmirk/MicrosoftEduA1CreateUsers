from string import Template

import requests
import json


FITST_USER_NAME = "mjj002" #刚刚 注册时候的用户名
OUTPUT_FILE_NAME = "facultys.txt" # 输出文件名


url = "https://admin.microsoft.com/admin/api/users"


payloadJsonFile = open("payload.json")
cookieJsonFile = open("cookie")
ajaxsessionkeyJsonFile = open("ajaxsessionkey")

payloadTxt  = str(payloadJsonFile.read()).strip()
ajaxsessionkey = str(ajaxsessionkeyJsonFile.read()).strip()
cookie = str(cookieJsonFile.read()).strip()
studentCount=0
file = open(OUTPUT_FILE_NAME,"w")
class User():
    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd





def writeLine(user):
    file.writelines("%s , %s\n"%(user.name,user.pwd))
    file.flush()
# both role
def createUser(userName):
    if payloadTxt == "":
        print("请填写 payload.json 文件")
        return
    if cookie=="":
        print("请填写 cookie 文件")
        return
    if ajaxsessionkey=="":
        print("请填写 ajaxsessionkey 文件")
        return



    global studentCount
    studentCount = studentCount + 1
    print(studentCount)

    payload = payloadTxt.replace(FITST_USER_NAME, userName)

    headers = {
        'authority': "admin.microsoft.com",

        'accept': "application/json, text/plain, */*",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        'ajaxsessionkey': ajaxsessionkey,
        'content-length': "23176",
        'Content-Type': "application/json",
        'cookie':cookie ,
        'origin': "https://admin.microsoft.com",
        'referer': "https://admin.microsoft.com/Adminportal/Home",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        'x-adminapp-request': "/users",
        'x-portal-consumerlogin': "False",
        'x-portal-routekey': "eas",
        'Cache-Control': "no-cache",
        'Host': "admin.microsoft.com",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=Template(payload).safe_substitute({"userName":userName}), headers=headers)

    print(response.text)
    passwd = json.loads(response.text)["AdditionalMessageInfo"]["Password"]

    writeLine(user=User(userName,passwd))
    createUser(passwd)



createUser("0000001")
