#Importing the ABC and abstractmethod from the abc module to create an abstract class
from abc import ABC , abstractmethod

#Creating an abstract class Shape which will be inherited by the child classes Circle, Square and Triangle
class Shape(ABC):

    def __init__(self,name):       #Creating a constructor to initialize the name of the shape
        self.name=name

    @abstractmethod                #Decorators
    def area(self):               #Defining the method area which will be overridden
        pass

class Circle(Shape):
    
    def __init__(self,name,radius):      #crating a costructor to initialize the radius of the class
        super().__init__(name)
        self.radius=radius

    
    def area(self):              #Overriding area of the parent class
        return 3.14*self.radius*self.radius
    
class Square(Shape):

    def __init__(self,name,side):       ##crating a costructor to initialize the side of the class 
        super().__init__(name)
        self.side=side
    
    def area(self):               ##Overriding area of the parent class    
        return self.side*self.side
    
class Triangle(Shape):

    def __init__(self,name,base,height):  ##crating a costructor to initialize the base and height of the class
        super().__init__(name)
        self.base=base
        self.height=height
    
    def area(self):              ##Overriding area of the parent class    
        return self.base*self.height*0.5
    
shapes=[Circle("Circle",5),Square("Square",12),Triangle("Triangle",3,8)]   #cerating the list
for shape in shapes:
    print(f"Area of the {shape.name} is {shape.area()}cm².")    #printing the overidden area of all the shapes