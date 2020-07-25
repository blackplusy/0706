#coding=utf-8

class animal:
    def jiao(self):
        print('aowu')

class dog(animal):
    def jiao(self):
        print('wang!!!')

class cat(animal):
    def jiao(self):
        print('miao!!!!')

def test(s):
    s.jiao()

a=animal()
a.jiao()
b=dog()
test(b)
c=cat()
test(c)