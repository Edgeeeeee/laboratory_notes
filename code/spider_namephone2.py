'''
2019/4/29
抓取老师手机号的代码
'''

import requests  # 请求网页的
import re  # 正则表达式
import json


def get_phone_from_html(html):  # 从html中得到phone
    ans1 = re.findall('="white-space:nowrap;" title="(.*)?">', html)
    ans2 = re.findall('<span style="color:#333333;width: 60px;">电话：</span>\r\n(.*)</li>', html)
    if len(ans1) > 0:
        return ans1[0].strip()
    if len(ans2) > 0:
        return ans2[0].strip()
    return 'no phone'


if __name__ == '__main__':
    url = 'http://homepage.hrbeu.edu.cn/irisweb/manage/resume/search/ajaxSearchByLetterNewPage'
    data = dict() # 空表单

    for word in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        data['letter'] = word
        res = requests.post(url, data=data)
        re_ans = re.findall('JSON.parse\(\'(.*)\'\);', res.text)
        teachers = json.loads(re_ans[0])

        for each_teacher in teachers['personList']:
            zhNamePy = each_teacher['zhNamePy']
            teacher_name = each_teacher['zhName']
            teacher_url = 'http://homepage.hrbeu.edu.cn/web/'+zhNamePy
            teacher_html = requests.get(teacher_url)
            if teacher_html.status_code == 404:
                print(teacher_name, 404)
                continue
            phone = get_phone_from_html(teacher_html.text)
            print(teacher_name, phone)
        
