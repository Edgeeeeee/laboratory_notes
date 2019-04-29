# 几个零散的知识点
- [python列表去除重复元素](https://www.cnblogs.com/chjbbs/p/5729540.html)
- [python垃圾回收机制](https://www.cnblogs.com/Xjng/p/5128269.html)
- [lambda](https://www.cnblogs.com/hf8051/p/8085424.html)
- return fun_name: 返回一个函数 
- locals() 返回当前作用域所有的变量（字典形式）
- globals()
- del xxx : 释放xxx
- a is xxx : 判断a和xxx是不是指向同一个内存
-
	a = 'xxx'
	b = 'xxx'
	a is b
	>>> True
	python对段字符串和整数声明时进行优化，省内存
	当b发生变化时，a，b就指向同一块内存了
# 作用域
- L(local):局部作用域
	- 只是在类，函数中定义。在if，for, while 中都不会形成局部作用域
- E(enclosing): 嵌套作用域
	- [闭包](https://www.cnblogs.com/JohnABC/p/4076855.html )：函数里定义函数。返回最内部的函数。
		- 保存运行状态，保存局部作用域
- G(global): 全局作用域
- B(built-in)：内置作用域
	- 最大的作用域，在全局作用之外，解释器定义好的，可以直接调用

- 举例(会报错)
- 
	num = 4
	def fun():
		num += 1 
	fun()
	print(num)
	>>> Error 
	在小作用域中访问大作用域只读不可写
### 解决方法
- global关键字  
	- 在小作用域中声明全局作用域变量，可读可写

- nonlocal
	- 打通闭包内变量作用域限制。


# 内存管理机制（百度）
- 引用计数法(百度)
	- 当对象被创建时候，引用次数变为+1  # a = 1
	- 对象被引用+1  # b = a
	- 对象当作参数 +1  # fun(a)
	- 对象进了容器 +1  # arr.append(a)
	- 对象别名被显示销毁-1  # del a
	- 对象名字被指向其他对象-1  # b = 'hello' a - 1
	- 对象离开了作用域-1
	- 对象离开容器-1  # arr.pop()
- 引用计数法的漏洞
	- 当变量被循环引用时，引用次数不会变成0
		- arr.append(brr） 
		- brr.append(arr)
	- 解决方法
		- [标记清除法](百度https://www.cnblogs.com/saolv/p/8411993.html)
			- 死亡容器(百度)
			- 存货容器(百度)
	- 分代回收
		- 新建的为第0代
		- 每执行一个 __标记清楚__ 操作 代数加1
		- 代数越高的对象(存活越持久),进行‘标记删除’的时间间隔越长，
- sys.getrefcount():返回变量引用次数



# 爬虫
- 原理：(百度)
	- 1.抓到html requests.get(url)
	- 2.解析html，把下一步的链接找出来，放进urls数组 #  re or other ways
	- 3.从urls数组内取一个url进行第一步  # append
- module bs4.BeautifulSoup()(百度)


# 正则表达式
- (百度)
	