class Animal:
    alive=True
    def eat(self):
        print("this animal eats")
    def sleep(self):
        print("this animal sleeps")
    def move(self):
        print("this animal moves")

class fish(Animal):
    def swim(self):
        super().move()
        print("fish swim")

class bird(Animal):
    def fly(self):
        super().move()
        print("bird fly")

class horse(Animal):
    def run(self):
        super().move()
        print("horse runs")

my_fish=fish()
my_bird=bird()
my_horse=horse()

#printing methods and attribute from parent class
print(my_fish.alive)
my_bird.sleep()
my_horse.eat()

#printing methods from there own classes
my_bird.fly()
my_fish.swim()
my_horse.run()