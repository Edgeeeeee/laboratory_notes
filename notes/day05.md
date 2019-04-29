# 爬虫
## requests
- import requests : 爬虫基本模块
- a = requests.get('url')
- a.encoding = a.apparernt_encouding:解码（自动）
- a.encoding = 'utf-8': utf-8格式解码
## json
- import [json](https://www.runoob.com/python/python-json.html):
	- json.dumps(a): 把容器a转化成字符串
	- json.loads(a): 把串a转化成容器
	- 举例
	- 
			a = [1,2,3]
			b = json.dumps(a)
			c = json.loads(b)
			print(type(b))
			print(type(c))

			>>> <class 'str'>
			>>> <class 'list'>

- [字符串和json区别](https://blog.csdn.net/jim_007/article/details/79107888)

## re
- import re： 正则表达式库
- re.findall('短字符串','长字符串')
	- \d : 数字，
	- 例：如果想抓电话号，写11个\d即可
	- *：前一个字符0次或者无限次扩展
	- {x}：x为整数，表示前一个字符重复x次
	- [a,b,c,d]:表示在a,b,c,d内查找选择第一个符合的。
		- []内的内容要按ascii顺序排好
	- 匹配默认为贪婪匹配，
	- '?' 表示非贪婪匹配，放在防止贪婪匹配的结束字符的前面
	- （）：括号内表示需要的，其他的符号只是为了定位
	- ![avatar](C:\Users\qaz\Desktop\pycode\pic\re_operate1.png)
