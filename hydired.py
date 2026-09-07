class school:
    def a(self):
        print("school 1")
class student1(school):
    def b(self):
        print("student 1")
class student2(student1):
    def c(self):
        print("student2")
class std(student1,student2):
    pass

aa=school()



