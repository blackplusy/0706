#coding=utf-8

# class dog:
#     def __init__(self,name,color='black'):
#         self.name=name
#         self.color=color
#     def run(self):
#         print('狗富贵，互相旺！')
#
# class taidi(dog):
#     def set_name(self,name):
#         self.name=name
#     def eat(self):
#         print('im eating!!!')
#
# gou=taidi('taitan')
# print('名字是%s,颜色是%s'%(gou.name,gou.color))
# gou.run()
# gou.set_name('2ha')
# print('名字是%s,颜色是%s'%(gou.name,gou.color))

class dog:
    def sayHi(self):
        print('wang!!!!')
class keji(dog):
    def sayHi(self):
        print('ao~~~wu~~~')

dog1=keji()
dog1.sayHi()



