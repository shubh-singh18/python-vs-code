# Each class should have its own method and call all three methods from the Son object.

class grandfather:
    def grand(self):
        print("this is grandfather")
class father(grandfather):
    def father(self):
        super(). __init__()
        print("this is father")
class son(father):
    def  son(self):
      super(). __init__()
      print("this is son")
aa=son()
aa.grand()
aa.father()
aa.son()