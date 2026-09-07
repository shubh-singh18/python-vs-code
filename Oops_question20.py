# 20. Design an E-Commerce Discount System using polymorphism.
#     Create different discount classes such as PercentageDiscount,
#     FlatDiscount, and NoDiscount.
#     The checkout system should calculate the final price dynamically
#     based on the selected discount strategy.
class Percentagediscount:
    def discount(self, price):
        return price * 10 / 100


class Flatdiscount:
    def discount(self, price):
        return 500


class Nodiscount:
    def discount(self, price):
        return 0


price = 10000

choice = int(input("Enter a choice: "))

if choice == 1:
    d = Percentagediscount()

elif choice == 2:
    d = Flatdiscount()

else:
    d = Nodiscount()

b = d.discount(price)
f = price - b

print("price", price)
print("discount", b)
print("final_price", f)


