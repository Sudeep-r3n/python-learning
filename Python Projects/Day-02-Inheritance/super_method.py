#creating a class Shape
class Shape:
    def __init__(self,color,is_filled):  #Adding attributes like color and is_filled to the Shape class
        self.color=color                 # these attributes will be inherited by the derived classes
        self.is_filled=is_filled

    def display_info(self):            #Method to diplay information about the shape's color and whether it is filled or not
        print(f"Color of {self.name} is {self.color}")
        print(f"Is {self.name} filled : {self.is_filled}")

#creating a derived class called Circle that inherits from Shape

class Circle(Shape):

    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius
        self.name="Circle"

    def area(self):
        return 3.14*self.radius*self.radius
    

    def display_info(self):
        super().display_info()
        print(f"Area of {self.name} is {self.area()}")

class Square(Shape):

    def __init__(self,color,is_filled,side):
        super().__init__(color,is_filled)
        self.side=side
        self.name="Square"

    def area(self):
        return self.side*self.side
    
    def display_info(self):
        super().display_info()
        print(f"Area of {self.name} is {self.area()}")

class Triangle(Shape):

    def __init__(self,color,is_filled,base,height):
        super().__init__(color,is_filled)
        self.base=base
        self.height=height
        self.name="Triangle"

    def area(self):
        return self.base*self.height*0.5
    
    def display_info(self):
        super().display_info()
        print(f"Area of {self.name} is {self.area()}")



circle=Circle("red",True,7)
circle.display_info()
triangle=Triangle("black",True,4,3)
triangle.display_info()
square=Square("white",False,43)
square.display_info()