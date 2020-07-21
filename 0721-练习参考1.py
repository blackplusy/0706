#coding=utf-8
#1.
for i in range(-3,4):
    if i<0:
        a=abs(i)
    else:
        a=i
    print(a*' '+'*'*(7-2*a))
    #print(a)
#2.
    
#n=int(input('请输入一个数字'))
#c=n//2
#for i in range(-c,c+1):
#    a=-i if i<0 else i
#    print(' '*a+'*'*(n-a*2))

#3.圣杯
print('=='*10)
n=7
e=n//2
for i in range(-e,n-e):
    a=-i if i<0 else i
    print((e-a)*' '+'*'*(2*a+1))
    
