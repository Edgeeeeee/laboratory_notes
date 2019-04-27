'''
# 重名的被覆盖了！


f = open('students.txt',encoding = 'utf-8')
tup = ([],)
for line in f.readlines():
    t = line.strip().split("\t")
    dic[t[0]] = t

while True:
    name = input("请输入姓名")
    if name in dic:
        print(dic[name])
    else:
        print("不存在")

f.close
'''

f = open('students.txt',encoding = 'utf-8')
lines = f.readlines()
while True:
    name = input("input name：")
    a = 0
    for i in lines:
        if name in i.split('\t')[0]:
            a += 1
            print(i)            
    if a == 0:
        print("None")
f.close()
    
'''
f = open('students.txt',encoding = 'utf-8')
lines = f.readlines()
while True:
    name = input("input name：")
    a = 0
    for i in lines:
        if name in i:
            a += 1
            print(i)
        else:
    
f.close()
'''    