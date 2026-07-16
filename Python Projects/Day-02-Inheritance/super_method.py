class Shape:
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled

    def display_info(self):
        print(f"Color of {self.name} is {self.color}")
        print(f"Is {self.name} filled : {self.is_filled}")

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

class Triangle(Shape):

    def __init__(self,color,is_filled,base,height):
        super().__init__(color,is_filled)
        self.base=base
        self.height=height
        self.name="Triangle"



circle=Circle("red",True,7)
circle.display_info()