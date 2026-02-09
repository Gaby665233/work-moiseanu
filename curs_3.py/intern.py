from employee import Employee
class Intern(Employee):
    def __init__(self, name, email,project_assigned):
        super().__init__(name, email)
        self.project_assigned = project_assigned

    def send_email(self, subject, message):
        super().send_email(subject, message)
        print(f"Project assigned: {self.project_assigned}")
    
    def work_on_project(self):
        print(f"{self.name}is working on {self.project_assigned}")
