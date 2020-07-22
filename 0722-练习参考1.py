#coding=utf-8
dic={'admin':'123','user1':'123','heygor':'456'}
while 1:
    name=input('请输入您的用户名:')
    if name not in dic.keys() or len(name)==0 :
        print('请重新输入您的用户名')
    else:
        print('yes')
        while 1:
            password=input('请输入您的密码')
            if dic[name]==password:
                print('已经登录')
                break
            else:
                print('您的密码有误！')
        break
            
