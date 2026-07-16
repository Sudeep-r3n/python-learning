class Person:
    def __init__(self,name,age,roll_no):
        self.name=name
        self.age=age
        self.roll_no=roll_no

class Student(Person):
        
        def roll(self):
             print(f"Roll no of {self.name} is {self.roll_no}")

student1=Student("Sudeep",20,1)

print(student1.name)
print(student1.roll_no)
student1.roll()

    
        