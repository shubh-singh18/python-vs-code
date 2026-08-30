# create a suitable class structure usinga at least4 classes and demonstrate hybrid inheritance.
class Parent:
    def show_parent(self):
        print("I am parent")

class Teacher(Parent):
    def show_teacher(self):
        print("I am Teacher")

class Student(Parent):
    def show_student(self):
        print("I am student")

class Online_Teacher(Teacher,Student):
    def show_online(self):
        print("I am online teacher")

aa=Online_Teacher()
aa.show_parent()
aa.show_teacher()
aa.show_student()
aa.show_online()
