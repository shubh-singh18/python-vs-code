# 10. Online Notification System — Abstraction + Polymorphism

# Create an abstract class Notification with:

# send(message)

# Create:
# - EmailNotification
# - SMSNotification
# - PushNotification

# Requirements:
# - Each class should implement send() differently.
# - Create one common function to send a notification.
# - The function should work with any Notification object.
# - Use abstraction and polymorphism.

from abc import ABC,abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass
class Emailnotification(Notification):
    def send(self):
        print(" the notification of emailnotification")

class SMSnotification(Notification):
    