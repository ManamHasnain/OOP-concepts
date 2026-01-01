class Employee:
    company="NASA" #these here are class attributes as defined inside class, outside any method
    bonus=1000
    def __init__(self,name,salary,contract_year,company): #these all here are instance attribure as defined inside the init method with self parameter
        self.name=name
        self.salary=salary
        self.contract_year=contract_year
        self.company=company

emp1=Employee("ali",34000,4,"Tesla")
print(emp1.company) #if instance attribute is present so it will be always printed, if not present then class attribute will be printed
print(emp1.bonus)
#in order to print class attribute, we will use class name and print that class attribute
print(Employee.company) #here now always class attribute will be printed


#Object Introspection: Getting Info about all the attributes and methods inside an particular object
print(dir(Employee)) #We also use dir method in case to find about all method in module
