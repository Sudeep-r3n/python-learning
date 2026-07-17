#Creating a base class Animal
class Animal:

    def __init__(self,name):         #Creating a constructor to initialize the name of the animal
        self.name=name
        
    def sound(self):                 #defining a method sound which will be overridden by the child classes
        print(f"Animal makes a sound")

#Creating the child classes Dog and Cat which inherit from the base class Animal
class Dog(Animal):

    def sound(self):     #Overriding the sound method of the base class Animal
        print(f"bhau")

class Cat(Animal):

    def sound(self):     #Overriding the sound method of the base class Animal
        print(f"meows")

animals=[Dog("Buddy"),Cat("Whiskers")]      #creating a list of animals and initializing them with the name of the animal
for animal in animals:
    print(f"{animal.name} says: ",end="")
    animal.sound()                 #Calling the sound method for each animal in the list