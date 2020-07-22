#coding=utf-8
#1.无参数无返回值
'''
def jia():
    num1=int(input('请输入第一个数字'))
    num2=int(input('请输入第二个数字'))
    print(num1+num2)
jia()

#2.无参数，有返回值
def login():
    username=input('your name:')
    return username
name=login()
print(name)
'''
#3.有参数，无返回值
def login(name,passwd):
    if len(name)>=5:
        print('合理！')
        if passwd=='123':
            print('登录成功')
        else:
            print('密码有误')
    else:
        print('不合理')
login('simida','123')
#4.有参数，有返回值
def click(name):
    if len(name)!=0:
        return 'success!'
    else:
        return 'failed!'

c=click('test')
print(c)

















