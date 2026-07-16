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

    def __init__(self,color,is_filled,radius):     #Adding an additional attribute radius to the Circle class
        super().__init__(color,is_filled)
        self.radius=radius
        self.name="Circle"

    def area(self):               #Method to calculate the area of the circle using the formula πr^2
        return 3.14*self.radius*self.radius
    

    def display_info(self):         #Method to display information about the circle, including its area
        super().display_info()
        print(f"Area of {self.name} is {self.area()}")

#creating a derived class called Square inherits from Shape
class Square(Shape):

    def __init__(self,color,is_filled,side):         #Adding an additional attribute side to the Square class
        super().__init__(color,is_filled)
        self.side=side
        self.name="Square"

    def area(self):                          #Method to calculate the area of the square using the formula side^2
        return self.side*self.side
    
    def display_info(self):                  #Method to display information about the square, including its area
        super().display_info()
        print(f"Area of {self.name} is {self.area()}")

#creating a derived class called Triangle that inherits from Shape
class Triangle(Shape):

    def __init__(self,color,is_filled,base,height):         #Adding additional attributes base and height to the Triangle class
        super().__init__(color,is_filled)
        self.base=base
        self.height=height
        self.name="Triangle"

    def area(self):                    #Method to calculate the area of the triangle using the formula 0.5*base*height
        return 0.5*self.base*self.height
    
    def display_info(self):         #Method to display information about the triangle, including its area
        super().display_info()
        print(f"Area of {self.name} is {self.area()}")  



