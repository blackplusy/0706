#coding=utf-8
import csv
#读文件
with open('F:\\1.csv','r') as f:
    reader=csv.reader(f)
    for i in reader:
        print(i)
        print(type(i))

#写文件
with open('F:\\2.csv','w') as f:
    file=csv.writer(f,dialect='excel')
    #写入文件常用方式writerow
    file.writerow([5,6,7])
    file.writerow([7,8,9])
print('OK')
