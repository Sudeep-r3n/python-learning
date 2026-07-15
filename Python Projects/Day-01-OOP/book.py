class book:

    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def display(self):
        print(f"title : {self.title}")
        print(f"author : {self.author}")
        print(f"price : {self.price}")