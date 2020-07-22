#coding=utf-8
#1.实参位置
def info(name,age):
    print('你的名字是%s ,你的年龄是 %d' % (name,age))

info('o8ma',18)

#2.关键字参数
def animal(pet1,pet2):
    print(pet1+'wang！！！'+pet2+'miao!!!')
animal('dog',pet2='cat')
animal(pet2='jiafei',pet1='wangcai')

#3.参数默认值
def userinfo(name,age,minzu='汉'):
    print('your name is %s,%d,民族:%s'%(name,age,minzu))

userinfo('ladeng',80)
userinfo('o8ma',30,'v5er')

#4.不定长参数
def test(x,y,*args):
    print(x,y,args)
test(1,2,'o8ma','ladeng')

def test1(x,y,**args):
    print(x,y,args)

test1(1,2,a=10,b='gaga')
