class Employee:
    def __init__(self,name,salary,contract_year):
        self.name=name
        self.salary=salary
        self.contract_year=contract_year

    def get_info(self):
        print(f"The name of the Employee is {self.name}, and his salary is {self.salary} and he has contract of {self.contract_year} years")

    def get_salary(self):
        return self.salary

emp1=Employee("ali",50000,4)
emp2=Employee("hassan",60000,3)

print("Employee 1 details")
emp1.get_info()

print("Employee 2 details")
emp2.get_info()
print("the salary of employee is ",emp2.get_salary())



