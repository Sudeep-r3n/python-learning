from abc import ABC, abstractmethod


class BankAccount(ABC):
    """Abstract base class for a generic bank account."""

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    @abstractmethod
    def deposit(self, amount: float) -> None:
        """Deposit money into the account."""
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        """Withdraw money from the account."""
        pass

    @abstractmethod
    def get_account_type(self) -> str:
        """Return the type of bank account."""
        pass

    def display_balance(self) -> None:
        """Print current account balance and owner."""
        print(f"Account owner: {self.owner}")
        print(f"Account type: {self.get_account_type()}")
        print(f"Current balance: ${self.balance:.2f}")


class CheckingAccount(BankAccount):
    """Concrete checking account implementation."""

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_account_type(self) -> str:
        return "Checking"


class SavingsAccount(BankAccount):
    """Concrete savings account implementation."""

    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def add_interest(self) -> None:
        """Apply interest to the savings balance."""
        self.balance += self.balance * self.interest_rate

    def get_account_type(self) -> str:
        return "Savings"


if __name__ == "__main__":
    # Example usage of the bank account system
    checking = CheckingAccount("Alice", 500.0)
    savings = SavingsAccount("Bob", 1000.0, interest_rate=0.03)

    checking.deposit(200.0)
    checking.withdraw(150.0)
    savings.add_interest()

    checking.display_balance()
    print()
    savings.display_balance()
