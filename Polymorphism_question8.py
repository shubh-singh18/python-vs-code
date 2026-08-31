# 9. Create a Bill class with a calculate_bill() method that calculates the bill for 1 item, 2 items, or 3 items.
class Bill:
    def calculate_bill(self,apple,banana=0,graphs=0):
        total_bill=apple+banana+graphs
        print("total_bill",total_bill)

aa=Bill()
aa.calculate_bill(100)
print()
aa.calculate_bill(100,80)
print()
aa.calculate_bill(100,80,120)
print()