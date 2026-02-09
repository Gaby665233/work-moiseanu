from employee import Employee

class SalesManager(Employee):
    def __init__(self, name, email, sales_target):
        super().__init__(name, email)
        self.sales_target = sales_target

    def track_sales(self):
        print(f"{self.name} is tracking sales towards the target of {self.sales_target}")
        