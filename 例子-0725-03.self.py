#coding=utf-8
class student:
    def __init__(self,name):
        self.name=name
    def info(self):
        print('你的名字是%s'% self.name)

def studentinfo(s):
    s.info()

heygor=student('黑哥GAGA')
#heygor是student实例化的对象
#对象实例化之后可以调用类的方法
studentinfo(heygor)
#studentinfo括号中传入heygor是一个已经实例化的对象，可以调用类的方法
#注意:函数可以传入常规数据，也可以传入对象

