from abc import ABC, abstractmethod


class Payment(ABC):
    """Abstract base class for different payment methods."""

    @abstractmethod
    def pay(self, amount):
        """Process a payment of the given amount.

        Subclasses must implement this method to handle payment
        processing for a specific payment type.
        """
        pass


class CreditCard(Payment):
    """Credit card payment implementation."""

    def pay(self, amount):
        # Simulate paying with a credit card
        return f"Paid {amount} using credit card."


class UPI(Payment):
    """UPI payment implementation."""

    def pay(self, amount):
        # Simulate paying with UPI
        return f"Paid {amount} using UPI."


class Cash(Payment):
    """Cash payment implementation."""

    def pay(self, amount):
        # Simulate paying with cash
        return f"Paid {amount} in cash."
