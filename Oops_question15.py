# 15. Create a Notification System using polymorphism.
#     Implement EmailNotification, SMSNotification, and PushNotification.
#     Each notification type should have its own send() implementation

class Notification_system:
    def notification(self,message):
        pass

class EmailNotification(Notification_system):
    def notification(self,message):
        print("Emailnotification",message)

class SMSNotification(Notification_system):
    def notification(self, message):
     print("SMSNotification",message)

class Pushnotification(Notification_system):
    def  notification(self, message):
        print("Pushnotification",message)

aa=EmailNotification()
aa.notification("hello how are you")
ab=SMSNotification()
ab.notification("hey ,kaise ho")
ac=Pushnotification()
ac.notification("what's up")



