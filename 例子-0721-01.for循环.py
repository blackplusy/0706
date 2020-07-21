#coding=utf-8

#字符串

for i in 'abc':
    print(i)
# 1.i='a'
# 2.i='b'
# 3.i='c'


#列表
l1=[1,2,'simida','baga']
for a in l1:
    print(a)

#函数
#内置函数range()
#range(10)          0-9
#range(1,10)        1-9
for i in range(1,10):
    print(i*'*')

for i in range(-5,5):
    #print(i)
    if i<0:
        print(-i)
    else:
        print(i)
