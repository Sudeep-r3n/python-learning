#creating a simple Bank Account class with inheritance
class Account:
    def __init__(self, account_number, account_holder, balance=0):   #Adding attributes like account number, account holder and balance to the Account class
        self.account_number = account_number        
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):     #Method to deposit money into the account, increasing the balance by the specified amount
        self.balance += amount

    def withdraw(self, amount):    #Method to withdraw money from the account, decreasing the balance by the specified amount if sufficient funds are available
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):         #Method to retrieve the current balance of the account
        return self.balance

#creating a derived class called SavingsAccount that inherits from Account
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):      #Adding an additional attribute interest_rate to the SavingsAccount class, with a default value of 0.02 (2%)
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):        #Method to add interest to the account balance based on the interest rate, increasing the balance by the calculated interest amount
        self.balance += self.balance * self.interest_rate