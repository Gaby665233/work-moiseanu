# Ne vom imagina că Alex lucrează la dezvoltarea sistemului de gestionare a angajaţilor în companie. El a creat clase pentru diferite/
#  tipuri de angajaţi, inclusiv SalesManager, DataAnalyst şi Intern. /
# Fără moştenire, codul lui arată astfel:

class SalesManager:
    def __init__(self, name, email, sales_target):
        self.name = name
        self.email = email
        self.sales_target = sales_target

    def send_email(self, subject, message):
        print(f"Sending email to {self.email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")

    def track_sales(self):
        print(f"{self.name} is tracking sales towards the target of {self.sales_target}")