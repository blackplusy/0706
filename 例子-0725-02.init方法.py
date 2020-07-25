#coding=utf-8
# class student:
#     def __init__(self):
#         self.boy=20
#         self.girl=30
#     def study(self):
#         print('im study')
#
# #实例化对象
# stu=student()
# print(stu.boy)
# print(stu.girl)

class student:
    def __init__(self,boy,girl):
        self.badboy=boy
        self.cutegirl=girl
    def study(self):
        print('im study!!')

z=student(30,20)
print('男生%d个'% z.badboy)
print('女生%d个'% z.cutegirl)





