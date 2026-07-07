#polymorphism basic example
# class Animal:
#     def sound(self):
#         print("Animal makes sound")
# class dog(Animal):
#     def sound(self):
#         print("dog make sound bow bow!")
# class cat(Animal):
#     def sound(self):
#         print("cat makes sound meow meow")
# class cow(Animal):
#     def sound(self):
#         print("cow makes sound moo moo")

# my_dog=dog()
# my_cat=cat()
# my_cow=cow()

# my_dog.sound()
# my_cat.sound()
# my_cow.sound()

#second example of a company where employees recieve salary but each employee get salary through different process
class Employee:
    def __init__(self, name, department):
        self.name=name
        self.department=department
    def calculate_salary(self):
        print("Salary Calculation")
class Manager(Employee):
    def __init__(self,name, department, basic_salary, bonus):
        super.__init__(name,department)
        self.basic=basic_salary
        self.bonus=bonus
    def calculate_salary(self):
        super().salary_info()
        total= self.basic_salary+self.bonus
        print("Name : ",self.name)
        print("Position: Manager")
        print("Total : ",total)
        
class Developer(Employee):
    def __init__(self, name, department, hourly_rates, hours):
        super.__init__(name, department)
        self.hourly_rate=hourly_rates
        self.hours=hours
    def calculate_salary(self):
        super().calculate_salary()
        total=self.hourly_rate*self.hours
        print("Name : ",self.name)
        print("Position: Developer")
        print("total : ",total)

class Intern(Employee):
    def __init__(self, name, department, stipend):
        super().__init__(name, department)        
        self.stipend=stipend
    def calculate_salary(self):
        super().calculate_salary()
        print("Name : ",self.name)
        print("Position: Intern")
        print("total : ",self.stipend)

manager=Manager("ali","hr",100000,10000)
manager.calculate_salary()

developer=Developer("hassan","finance",10000,8)
developer.calculate_salary()

intern=Intern('fatima','administration',30000)
intern.calculate_salary()
        