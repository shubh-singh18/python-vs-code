# Employee Salary Calculator
# Write a function employee_salary(basic_salary) to calculate an employee's gross salary using:

# HRA = 20% of basic salary
# DA = 10% of basic salary
# Gross Salary = Basic + HRA + DA
# Menu-Driven Program Using Function
def employee_salary(basic_salary):
    gross_salary=0
    HRA=basic_salary*20/100
    DA=basic_salary*10/100
    gross_salary=HRA+DA+basic_salary
    return gross_salary
print(employee_salary(500000000000))


