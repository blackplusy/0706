#coding=utf-8
a=int(input('your num1'))
b=int(input('your num2'))
c=int(input('your num3'))

if a==b and b==c:
    print('等边三角形')
elif a==b or a==c or b==c:
    print('等腰三角形')
elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print('直角三角形')
else:
    print('普通')
