# 5. Student Result System — Encapsulation

# Create a Student class with:
# - name
# - roll_number
# - marks

# Requirements:
# - Marks should be private.
# - Create getter and setter methods for marks.
# - Marks must be between 0 and 100.
# - Calculate total marks.
# - Calculate percentage.
# - Display the student's complete result.

class Student:
    def __init__(self,name,roll_no,marks1,marks2,marks3):
        self.name=name
        self.roll_no=roll_no
        self.__marks1=marks1
        self.__marks2=marks2
        self.__marks3=marks3

    def setter(self,marks1,marks2,marks3):
        if 0<=marks1 <=100 and 0<=marks2 <=100 and 0<=marks3 <=100:
            self.marks1=marks1
            self.marks2=marks2
            self.marks3=marks3
        else:
            print("Invalid marks")

    def getter(self):
        return self.__marks1,self.__marks2,self.__marks3

    def result(self):
        total_marks=self.__marks1+self.__marks2+self.__marks3
        percentage=total_marks/3

        print("name",self.name)
        print("roll.no",self.roll_no)
        print("marks",self.getter())
        print("totalmarks",total_marks)
        print("percentage",percentage)

aa=Student("thakur",1001,90,98,99)
aa.setter(90,98,99)
aa.result()


