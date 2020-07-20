#coding=utf-8
#设置字符集
#字符集相当于翻译官
#中文编码字符集:GBK2312

#1.直接输出
# 数字  123
# 字符串 abc
# print()函数中输出内容
print('哈勒少！')
print(100)

#2.变量输出
#python中所有的符号都一定要是英文
#变量:可以变化的值，就是一个容器
a='告诉你妈妈晚上不回家，我给你看我写的代码！'
#a就是变量的名字
#引号里面就是变量的值
print(a)
a=100
print(a)
#变量操作后输出
a=200
b=300
print(a+b)
a='heygor'
b=' is no.1'
print(a+b)
a='100'
b='200'
print(a+b)

#3.函数输出
#系统中有很多自带函数，可以直接使用
# abs()  绝对值
# len()  长度
print(abs(-20))
s='爱你么么哒！'
print(len(s))

#4.格式化输出
#   %s   接受变量传入的字符类型数据
#   %d   接受变量传入的数值类型数据
#   输出内容如果只有变量值可以不加括号，超过1个一定要加括号
# 小红是no.1
# 小绿是no.2
# 小兰是no.3
name='heygor'
num=1
print('%s is no.%d'%(name,num))
name='lilei'
print('%s is no.%d'%(name,num))

print('您的名字是%s'% name)













