import requests
from bs4 import BeautifulSoup#不用也行，Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup就不能自动识别编码方式了。然后，你仅仅需要说明一下原始编码方式就可以了。Beautiful Soup已成为和lxml、html6lib一样出色的python解释器，为用户灵活地提供不同的解析策略或强劲的速度。
import json
import re
import time
url ="http://homepage.hrbeu.edu.cn/irisweb/manage/resume/search/ajaxSearchByLetterNewPage" 
a = requests.post(url)
html = BeautifulSoup(a.content,"html.parser").text.strip( )
# 爬虫

qq="\"zhName.*zounan\""
a = re.search(qq,html)
#正则找到表单

k = a.group().split("},{")#清洗数据
sjk={}
for i in k:
    z = i.replace(":",",").split(",")[1].strip("\"")
    if(z not in sjk):

        sjk[z] = ""
    try:
        v = i.replace(":",",").split(",")[5].strip("\"")
        sjk[z] = v
    except:#有些老师是没有的，得用另一种链接（psnCODE）访问，再说，略过。
        continue
#数据库(sjk{})存在了,姓名对应配音
d ={}#可以建立个字典，使得人名与电话有关系
for j in sjk:
    url2 ="http://homepage.hrbeu.edu.cn/web/{}".format(sjk[j]) #format格式化字符串，可以使{}里的被代替
    n = requests.post(url2)
    print(j,":")#老师名字
    Html = BeautifulSoup(n.content).select("font")
    for i in Html:
        time.sleep(0.1)#防止压力过大，休息一下
        if(re.match('^[01]\d{3}-',i.text) or re.match('^1\d{10}',i.text)):#正则找到电话或者手机号
            print(i.text)#如果存在，就可以打印出来
            break
    else:
        print("无")
