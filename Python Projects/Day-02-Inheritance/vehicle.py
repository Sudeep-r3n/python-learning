#creating a base class called Vehicle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make     #Adding attributes like make, model and year to the Vehicle class
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"   #Method to display vehicle information

#creating a derived class called Car that inherits from Vehicle 
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors): #Adding an additional attribute num_doors to the Car class
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        return f"{super().display_info()} with {self.num_doors} doors"   #Method to display car information, including the number of doors