#Creating the Parent class Employee with attributes name and salary
class Employee:

    def __init__(self, name, salary):    #Creating an init method to initialize the name and salary attributes
        self.name = name
        self.salary = salary

#Creating the Child class Manager that inherits from Employee
class Manager(Employee):

    def __init__(self, name, salary, department):    #Creating an init method to initialize the name, salary and department attributes
        super().__init__(name, salary)
        self.department = department

    def display_info(self):                          #Method to display information about the manager, including their name, salary and department they manage
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")