# Create a Parent class with a show() method. Create a Child class that inherits from Parent and call the parent method.

class Parent:
    def show(self):
        print("this is parent class")
class child(Parent):
    def show(self):
        print("this is child class")
        super().show()
aa=child()
aa.show()