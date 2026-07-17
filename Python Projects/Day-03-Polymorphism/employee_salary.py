# Base class for employees with a common salary calculation interface
class Employee:
    def __init__(self, name, base_salary):     
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        # For a basic employee, salary is just the base salary
        return self.base_salary


# Manager class inherits from Employee and adds a bonus
class Manager(Employee):
    def __init__(self, name, base_salary, bonus=0):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        # Manager salary includes the base salary plus bonus
        return self.base_salary + self.bonus


# Developer class inherits from Employee and adds overtime compensation
class Developer(Employee):
    def __init__(self, name, base_salary, overtime_hours=0, overtime_rate=0):
        super().__init__(name, base_salary)
        self.overtime_hours = overtime_hours
        self.overtime_rate = overtime_rate

    def calculate_salary(self):
        # Developer salary includes base salary plus overtime pay
        return self.base_salary + self.overtime_hours * self.overtime_rate


if __name__ == "__main__":
    # Example usage of the polymorphic employee salary classes
    manager = Manager("Alice", 80000, bonus=10000)
    developer = Developer("Bob", 70000, overtime_hours=10, overtime_rate=50)

    print(f"{manager.name} salary is: {manager.calculate_salary()}")
    print(f"{developer.name} salary is: {developer.calculate_salary()}")
