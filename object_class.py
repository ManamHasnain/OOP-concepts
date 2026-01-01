class Employee:
    company="HP"
    def get_salary(self): #self is mandatory here as it refers to the object of class being created
        salary=50000
        return salary

emp1=Employee() #an object emp1 created of the class Employee
emp2=Employee()

print("employee 1 details")
print(emp1.get_salary())

print("employee 2 details")
print(emp2.company)
print(emp2.get_salary())
