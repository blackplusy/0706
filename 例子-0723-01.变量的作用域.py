#coding=utf-8
#局部变量
def test():
    a=10
    print('修改前a的值',a)
    a=20
    print('修改后a的值',a)

def test1():
    a=40
    print('test1中a的值是',a)
    
test()
test1()
#全局变量
a=100
def test1():
    a=20
    print('test1中a的值',a)

def test2():
    print('test2中的值',a)

test1()
test2()
#修改全局变量
print('*'*20)
a=100
print('全局变量a的值',a)

def test1():
        global a
        a=200
        print('test1中修改全局变量a',a)
def test2():
    print('test2中使用全局变量',a)
test1()
test2()


    
