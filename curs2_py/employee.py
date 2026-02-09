class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def send_email(self, subject, message):
        print(f"Sending email to {self.email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")