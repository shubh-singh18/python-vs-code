#create father and mother classses with separeate methods. create a child class that inherits from both.
class Father:
    def father(self):
        print("father:I am engineer")
class Mother:
    def mother(self):
        print("mother: I am teacher")
class Child(Father,Mother):
    def child(self):
        print("child:I am student")

aa=Child()
aa.father()
aa.mother()
aa.child()