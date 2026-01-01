class Animal:
    location=(input("enter the location"))
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("this animal is speaking...")

class Dog(Animal): #dog is child class that has inherits all attributes and methods of animal class
    def speak(self):
        super().speak() #if want to show method of parent class through child class we use super()
        print("dog barks...")

my_dog=Dog("bruno")
print(my_dog.name)
print(my_dog.location)
my_dog.speak()