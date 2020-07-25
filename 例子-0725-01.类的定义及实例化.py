#coding=utf-8

class student:                       #创建一个类
    def study(self):                 #方法列表
        print('im study !!!!')       #方法列表中的逻辑
    def play(self):
        print('play ball!!!')

boy=student()
#产生一个student对象，通过boy实例对象来访问属性和方法
boy.age=10
#给对象添加属性
boy.faver='baseball'
#实例化对象boy调用类里面的方法
boy.study()
boy.play()

print(boy.age)
print(boy.faver)
