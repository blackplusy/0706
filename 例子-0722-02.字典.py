#coding=utf-8
dic={'name':'heygor','age':18}
dic1={'name':'o8ma'}
#直接访问
print(dic)
#数据筛选
print(dic['name'])
print(dic['age'])

#删除字典
#del
dic={'name':'heygor','age':18}
print(dic)
del dic['age']
print(dic)
del dic
#print(dic)
#clear
dic={'name':'heygor','age':18}
print(dic)
dic.clear()
print(dic)

#字典的修改
dic={'name':'5kong','age':1000}
print(dic)
dic['name']='8jie'
print(dic)
dic['age']=10
print(dic)
#keys
dic={'name':'5kong','age':1000}
print(dic.keys())
for i in dic.keys():
    print(i)
#values
dic={'name':'5kong','age':1000}
print(dic.values())
for i in dic.values():
    print(i)
#items
dic={'name':'5kong','age':1000}
print(dic.items())

for key,value in dic.items():
    print(key+':'+str(value))



