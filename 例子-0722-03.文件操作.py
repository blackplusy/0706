#coding=utf-8
#读文件
#定义一个变量接受open函数打开文件后的内容
file=open('f:\\1.txt','r',encoding='utf8')
print(file)
for i in file:
    print(i)
file.close()

#写文件
str1='oh my dear mom!!!'
file=open('f:\\2.txt','w')
file.write(str1)
file.close()
print('已经写入')

#追加文件
file=open('f:\\2.txt','a')
file.write('\ncome on baby!!!')
file.close()
print('执行完毕')
