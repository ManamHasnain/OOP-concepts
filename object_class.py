class Employee:
    #check getting input from user later
    # name=input("enter the name of employee")
    # company=input("enter the company name of employee")
    company="HP"
    def get_salary(self):
        salary=50000
        return salary

emp1=Employee()
emp2=Employee()

print("employee 1 details")
# print(emp1.name)
# print(emp1.company)
print(emp1.get_salary())

print("employee 2 details")
# print(emp2.name)
print(emp2.company)
print(emp2.get_salary())
