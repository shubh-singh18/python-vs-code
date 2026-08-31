# Create a Result class with a marks() method that accepts marks of 1 subject, 2 subjects, or 3 subjects and calculates the total.
class Result:
    def marks(self,hindi,english=0,maths=0):
        total_marks=hindi+english+maths
        print("total_marks",total_marks)

aa=Result()
aa.marks(60)
aa.marks(60,80)
aa.marks(60,80,70)