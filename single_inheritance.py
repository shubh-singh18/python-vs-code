#single Inheritance
class Teacher:
    def teacher(self):
        print("I am a teacher")

class Student(Teacher):
    pass
aa=Student()
aa.teacher()
