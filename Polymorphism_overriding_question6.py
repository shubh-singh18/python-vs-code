# Create a Bank class with an interest_rate() method. Create an SBI class that overrides it and returns SBI's interest rate.
class Bank:
    def interest_rate(self):
      return "Bank interest rate"

class SBI(Bank):
    def interest_rate(self):
        return "SBI interest rate"
aa=SBI()
print(aa.interest_rate())

