#Creating the Parent class Person with attributes name and age
class Person:

    def __init__(self,name,age):    #Creating an init method to initialize the name and age attributes
        self.name=name              #Adding attributes like Name and Age
        self.age=age

#Creating the Child class Student that inherits from Person
class Student(Person):

    def __init__(self,name,age,roll_no):  #Creating an init method to initialize the name, age and roll no attributes
        super().__init__(name,age)        #Using super() to call the init method of the parent class Person
        self.roll_no=roll_no              #Adding an additional attribute roll_no to the Student class

    def display_info(self):               #Method to display information about the student, including their name, age and roll number
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")
        print(f"Roll : {self.roll_no}")

#Creating the child class Teacher that inherits from Person
class Teacher(Person):

    def __init__(self,name,age,subject):  #Creating an init method to initialize the name, age and subject attributes
        super().__init__(name,age)        #Using super() to call the init method of the parent class Person
        self.subject=subject              #Adding an additional attribute subject to the Teacher class

    def display_info(self):               #Method to display information about the teacher, including their name, age and subject they teach
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Subject : {self.subject}")