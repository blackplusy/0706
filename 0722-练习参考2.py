#coding=utf-8
dic={'admin':'123'}
name=input('请输入用户名')
passwd=input('请输入密码')
#定义写入文件的方式，写入的内容，
def WriteFile(filename,text):
    file=open(filename,'a')
    file.write(text)
    file.close()
    print('OK')
    
def LogIn(name,passwd):
    if name in dic.keys():
        if dic[name]==passwd:
            WriteFile('yes.log',name+','+passwd)
            return 'success'
        else:
            WriteFile('no.log',name+','+passwd)
            return 'failed'
    else:
        return 'username is wrong'

p=LogIn(name,passwd)
print(p)
