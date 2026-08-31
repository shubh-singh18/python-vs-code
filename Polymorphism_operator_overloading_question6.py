# Time class banao aur + operator overload karke do time objects ko add karo.
# Example: 2 hr 30 min + 1 hr 45 min = 4 hr 15 min

class Time:
    def __init__(self,hr,min):
        self.hr=hr
        self.min=min
    def __add__(self,other):
        hr=self.hr+other.hr
        min=self.min+other.min

        if min>=60:
            hr=hr+1
            min=min-60
        return Time(hr,min)

    def display(self):
        print(self.hr,"hr",self.min,"min")

aa=Time(2,40)
ab=Time(4,50)
res=(aa+ab)
print(res.hr,"hr",res.min,"min")


