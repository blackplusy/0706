#coding=utf-8

num=int(input('请输入一个三位数'))
if (num//100)**3+(num%100//10)**3+(num%10)**3==num:
    print('%d is 水仙花'% num)
else:
    print('不是水仙花数字')
