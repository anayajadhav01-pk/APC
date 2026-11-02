class Notification:
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f'Sending Email: {message}')

class SMSNotification(Notification):
    def send(self, message):
        print(f'Sending SMS: {message}')

class PushNotification(Notification):
    def send(self, message):
        print(f'Sending Push Notification: {message}')

notifications = [EmailNotification(), SMSNotification(), PushNotification()]
for n in notifications:
    n.send('Your OTP is 492015')
