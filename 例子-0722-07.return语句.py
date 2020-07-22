#coding=utf-8
#一个返回值
#定义函数sum，需要传入2个参数
def sum(a,b):
    #业务逻辑，两个数字相加
    jisuan=a+b
    #返回计算结果
    return jisuan
#变量接受函数处理后的结果
a=sum(10,20)
print(a)
#多个返回值
def ret(a,b):
    a*=10
    b*=100
    return a,b
num=ret(5,7)
print(num)
print(type(num))

num1,num2=ret(40,80)
print(num1,num2)
    
