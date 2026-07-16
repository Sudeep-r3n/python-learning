#Defining Parent class
class Animal:

    def __init__(self,name):     #creating an init method to initialize the name and is_alive attributes
        self.name = name
        self.is_alive = True

    def sleep(self):             #creating methods like sleep and eat to display the animal's actions
        print(f"{self.name} is asleep")

    def eat(self):
        print(f"{self.name} is eating")

#Defining Child class
class Dog(Animal):
    def speak(self):       #Adding sound method to the Dog class
        print(f"{self.name} says woof woof")

class Cat(Animal):
    def speak(self):       #Adding sound method to the Cat class
        print(f"{self.name} says meow meow")

class Bird(Animal):        #Adding sound method to the Bird class
    def speak(self):
        print(f"{self.name} says chirp chirp")

