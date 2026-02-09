from employee import Employee
class SalesManager(Employee):
    def __init__(self, name, email,sales_target):
        super().__init__(name, email)
        self.sales_target = sales_target

    def send_email(self, subject, message):
        super().send_email(subject, message)
        print(f"Sales target for this quarter: {self.sales_target}")

    def get_role(self):
        return "Sales Manager"
    
    def track_sales(self):
        print(f"{self.name} is tracking sales towards the target of {self.sales_target}")
    
    def display_info(self):
        super().display_info()
        print(f"Sales Target: {self.sales_target}")