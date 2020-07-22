#coding=utf-8
#创建元组
tup=(1)
print(tup)
print(type(tup))

tup=(1,)
print(tup)
print(type(tup))
#访问元组
a=(1,2,3)
print(a)

for i in a:
    print(i)

if 3 in a:
    print('3 is here!')
#删除元组
a=(1,2,3)
del a
#print(a)
#元组的索引和切片
tup=(1,2,3,4,5)
print(tup[0])
print(tup[-2])
print(tup[2:4])
print(tup[3:])
print(tup[:3])
#补充
a=(1,2,3,3,3,3,3)
print(len(a))
print(max(a))
print(min(a))
print(a.index(3))
print(a.count(3))
