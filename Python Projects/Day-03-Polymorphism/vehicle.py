# Base class for all vehicles
class Vehicle:
    
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        # Common engine start behavior for all vehicles
        print(f"Starting engine of {self.make} {self.model}.")

    def stop_engine(self):
        # Common engine stop behavior for all vehicles
        print(f"Stopping engine of {self.make} {self.model}.")

    def move(self):
        # Generic move method to be overridden by subclasses
        print(f"The {self.make} {self.model} moves forward.")


# Derived class representing a car
class Car(Vehicle):
    def move(self):
        # Override move method for car-specific behavior
        print(f"The car {self.make} {self.model} drives on the road.")


# Derived class representing a truck
class Truck(Vehicle):
    def move(self):
        # Override move method for truck-specific behavior
        print(f"The truck {self.make} {self.model} hauls cargo down the highway.")


# Derived class representing a motorcycle
class Motorcycle(Vehicle):
    def start_engine(self):
        # Override start_engine method for motorcycle-specific behavior
        print(f"Revving the motorcycle {self.make} {self.model} engine.")

    def move(self):
        # Override move method for motorcycle-specific behavior
        print(f"The motorcycle {self.make} {self.model} speeds along the road.")


if __name__ == '__main__':
    vehicles = [
        Car('Toyota', 'Camry'),
        Truck('Ford', 'F-150'),
        Motorcycle('Harley-Davidson', 'Sportster')
    ]

    for vehicle in vehicles:
        vehicle.start_engine()
        vehicle.move()
        vehicle.stop_engine()
        print()