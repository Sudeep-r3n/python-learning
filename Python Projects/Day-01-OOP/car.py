class car:

    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def display_info(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Year  : {self.year}")