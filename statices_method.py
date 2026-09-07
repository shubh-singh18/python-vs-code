# class student:

#     @staticmethod
#     def hello():
#         print("hello")
# s=student.hello()

# class s:
#     a="sun"
#     @staticmethod
#     def add():
#         print(s.a)
# s.add()

# class s:
#     name="shubh"
#     branch="cse"
#     year="2026"
#     @staticmethod
#     def a():
#         print(s.name,s.branch,s.year)
# s.a()


# 4. Product Class
# Create a Product class with:
# - store_name as class variable
# - name and price as instance variables
# - display() as instance method
# - change_store() as class method
# - check_price() as static method

class Product():
     store_name="vodka"
     def __init__(self,name,price):
          self.name=name
          self.price=price
    

     def display(self):
          print(f"name{self.name},price{self.price}")

     @classmethod 
     def aa(cls,ss):
        cls.store_name=ss
        print(cls.store_name)

     @staticmethod
     def check_price(price):
          return price>0

aa=Product("Fratelli J'Noon Red",5800000)
aa.display()
Product.aa("wine")
print(Product.check_price(4500))




          