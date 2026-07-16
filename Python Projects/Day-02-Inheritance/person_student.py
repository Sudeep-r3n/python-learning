# Creating the Parent class
class Person:

    def __init__(self,name,age,roll_no): #creating an init method to initialize the name, age and roll no attributes
        self.name=name         #Adding attributes like Name ,Age and Roll no
        self.age=age
        self.roll_no=roll_no

#creating Child class
class Student(Person):
        # defing one more metod to get roll no with the name
        def roll(self):
             print(f"Roll no of {self.name} is {self.roll_no}")   #printing the roll no of the student with the name


    
        