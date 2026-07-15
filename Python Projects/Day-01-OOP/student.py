class student:

    class_year=2026
    num_students=0

    def __init__(self,name,roll_no,marks):
        self.name= name
        self.marks= marks
        self.roll_no= roll_no
        student.num_students+=1

    def display(self):
        print(f"Name : {self.name}" )
        print(f"Roll  : {self.roll_no}" )
        print(f"Marks : {self.marks}" )




