#coding=utf-8
#直接访问
l=['李元芳','李白','钟馗']
print(l)
#遍历访问
for i in l:
    print(i)
#成员访问
if '张小敬' in l:
    print('is here')
else:
    print('not here!')
#列表的索引和切片
l1=['黄忠','赵云','关羽','马超','张飞']
print(l1[0])
print(l1[-2])
#print(l1[5])
print(l1[2:])
print(l1[2:3])
#列表的拼接
l=[1,2,3,4]
m=['a','b']
print(l+m)
#列表的更新(修改)
l=[1,2,3]
print(l)
l[2]='柳岩'
print(l)
l[-2]='离线'
print(l)

#列表的删除
l=[1,2,3]
print(l)
del l[2]
print(l)










