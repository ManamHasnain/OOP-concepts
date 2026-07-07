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
# class Employee:
#     def __init__(self, name, department):
#         self.name=name
#         self.department=department
#     def calculate_salary(self):
#         print("Salary Calculation")
# class Manager(Employee):
#     def __init__(self,name, department, basic_salary, bonus):
#         super().__init__(name,department)
#         self.basic_salary=basic_salary
#         self.bonus=bonus
#     def calculate_salary(self):
#         super().calculate_salary()
#         total= self.basic_salary+self.bonus
#         print("Name : ",self.name)
#         print("Position: Manager")
#         print("Total : ",total)
        
# class Developer(Employee):
#     def __init__(self, name, department, hourly_rate, hours):
#         super().__init__(name, department)
#         self.hourly_rate=hourly_rate
#         self.hours=hours
#     def calculate_salary(self):
#         super().calculate_salary()
#         total=self.hourly_rate*self.hours
#         print("Name : ",self.name)
#         print("Position: Developer")
#         print("total : ",total)

# class Intern(Employee):
#     def __init__(self, name, department, stipend):
#         super().__init__(name, department)        
#         self.stipend=stipend
#     def calculate_salary(self):
#         super().calculate_salary()
#         print("Name : ",self.name)
#         print("Position: Intern")
#         print("total : ",self.stipend)

# manager=Manager("ali","hr",100000,10000)
# manager.calculate_salary()

# developer=Developer("hassan","finance",10000,8)
# developer.calculate_salary()

# intern=Intern('fatima','administration',30000)
# intern.calculate_salary()

#third real world example of Polymorphism
#online shopping payement system
class Payement:
    def __init__(self,amount):
        self.amount=amount
    def pay(self):
        print("payement processing")
class Credit_Card(Payement):
    def pay(self):
        super().pay()
        print("Payement method: Credit Card")
        print("Amount : ",self.amount)
        print("Payement successful via Credit Card")
class PayPal(Payement):
    def pay(self):
        super().pay()
        print("Payement method: PayPal")
        print("Amount : ",self.amount)
        print("Payement successful via PayPal")
class BankTransfer(Payement):
    def pay(self):
        super().pay()
        print("Payement method: Bank Transfer")
        print("Amount : ",self.amount)
        print("Payement successful via Bank Transfer")
# payement1=Payement(20000)
# payement1.pay()
payement2=Credit_Card(2000)
payement2.pay()
payement3=PayPal(890)
payement3.pay()
payement4=BankTransfer(9870)
payement4.pay()

