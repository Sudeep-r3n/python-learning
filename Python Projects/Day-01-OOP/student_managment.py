class Student:


    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display_info(self):
        print(f"Name  : {self.name}")
        print(f"Roll  : {self.roll}")
        print(f"Marks : {self.marks}")

# Taking input
Name = input("Enter the name of student : ")
Roll = input("Enter the Rollno of the student : ")
Marks = input("Enter the marks of the student : ")


student = Student(Name, Roll, Marks)

student.display_info()

