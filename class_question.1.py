# class student:
#     def ss(self,*args):
#         print(*args)
# aa=student()
# aa.ss("shubh")
# aa.ss("shubh","cse")   

class a:
    def bb(self,name,branch):
        name=name
        branch=branch
        print(name,branch)
class b(a):
    def bb(self,name,branch):
        super(). __init__(name,7)
obj=b()
obj.bb("shubh","cse")
obj.bb("shubh","cs")


