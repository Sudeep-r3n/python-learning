from abc import ABC, abstractmethod


class Notification(ABC):
    """Abstract base class for notification channels."""

    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        """Send a notification to the recipient."""
        pass


class EmailNotification(Notification):
    """Notification implementation for email."""

    def send(self, recipient: str, message: str) -> None:
        # In a real system, integrate with an email provider/API here.
        print(f"Sending Email to {recipient}: {message}")


class SMSNotification(Notification):
    """Notification implementation for SMS."""

    def send(self, recipient: str, message: str) -> None:
        # In a real system, integrate with an SMS gateway here.
        print(f"Sending SMS to {recipient}: {message}")


class WhatsAppNotification(Notification):
    """Notification implementation for WhatsApp."""

    def send(self, recipient: str, message: str) -> None:
        # In a real system, integrate with WhatsApp Business API here.
        print(f"Sending WhatsApp to {recipient}: {message}")


class NotificationManager:
    """Manager to handle sending notifications through different channels."""

    def __init__(self, notification: Notification) -> None:
        self.notification = notification

    def notify(self, recipient: str, message: str) -> None:
        """Send a message using the configured notification channel."""
        self.notification.send(recipient, message)


if __name__ == "__main__":
    # Example usage of the notification system with different channels.
    email_notifier = NotificationManager(EmailNotification())
    sms_notifier = NotificationManager(SMSNotification())
    whatsapp_notifier = NotificationManager(WhatsAppNotification())

    email_notifier.notify("user@example.com", "Your order has been shipped.")
    sms_notifier.notify("+1234567890", "Your verification code is 123456.")
    whatsapp_notifier.notify("+1234567890", "Hello from the WhatsApp notification system.")
