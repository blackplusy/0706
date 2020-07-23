#coding=utf-8
import os
import sys
#os.system('dir')    #运行系统中的命令 dir
#os.system('tasklist')
#os.remove('F:\\1.txt')  #删除系统中的文件
print(os.getcwd())       #当前文件夹的绝对路径
print(os.listdir('F:'))  #指定文件夹下所有文件名
print(os.path.split('F:\\1\\2.txt'))  #返回一个路径的目录和文件名
print(os.path.isfile('F:\\1\\2.txt')) #判断是否是文件
#os.path.isdir()   判断是否是目录
#os.path.exists()  判断是否存在

print(sys.version)
print(sys.path)
