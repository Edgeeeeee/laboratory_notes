# 姓名	性别	学院	班级	中学	外语语种	班级号	生源地
'''


f = open("students.txt",encoding = 'utf-8')
# f = readlines("student")
# print(len(f))
li = []
for line in f.readlines():
    t = line.strip().split("\t")
    li.append(t[1])
man = 0
woman = 0
for i in li:
    if i == "男":
        man += 1
    if i == '女':
        woman += 1 
print("man:{}".format(man))
print("woman{}".format(woman))


'''
'''

f = open('students.txt',encoding = 'utf-8')
dic = {}
for line in f.readlines():
    t = line.strip().split("\t")
    if (t[2]+' 男') in dic and t[1] == "男":
        dic[(t[2]+" 男")] += 1 
    if (t[2]+' 女') in dic and t[1] == "女":
        dic[(t[2]+' 女')] += 1
    if (t[2]+' 男') not in dic and t[1] == "男":
        dic[(t[2]+" 男")] = 1
    if (t[2]+' 女') not in dic and t[1] == "女":
        dic[(t[2]+' 女')] = 1

print(dic)
for k,v in dic.items():
    print(k,"---",v)
'''



f = open('students.txt',encoding = 'utf-8')
dic = {}
for line in f.readlines():
    t = line.strip().split("\t")
    if t[1] == "男" and t[2] in dic:
        dic[t[2]][0] += 1
    elif t[1] == "女" and t[2] in dic:
        dic[t[2]][1] += 1
    elif t[1] == "男" and t[2] not in dic:
        dic[t[2]] = [1,0]
    elif t[1] == "女" and t[2] not in dic:
        dic[t[2]] = [0,1]


for k,v in dic.items():
    print(k,":",v)
