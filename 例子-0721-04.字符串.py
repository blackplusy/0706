#coding=utf-8
#1.索引
name='im your papa!'
print(name[0])
print(name[3])
print(name[-2])
#print(name[30])
#2.切片
name='im your papa!'
print(name[0:4])
print(name[:4])
print(name[4:])
print(name[3:-1])
#3.其他操作
#拼接
a='lady'
b='gaga'
print(a+b)
tel='0452-1111111'
print(tel[:5])
print(tel[5:])
print(tel[:5]+'6'+tel[5:])
#遍历
name='im your papa!'
for i in name:
    print(i)
#去空格
#string.strip() 去掉两边的空格
#string.lstrip() 去掉左边的空格
#string.rstrip() 去掉右边的空格
str1='   python    '
print(str1)
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())
#计算长度
str1='   python    '
print(len(str1))
















