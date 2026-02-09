class Intern:
    def __init__(self, name, email, project_assigned):
        self.name = name
        self.email = email
        self.project_assigned = project_assigned

    def send_email(self, subject, message):
        print(f"Sending email to {self.email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")

    def work_on_project(self):
        print(f"{self.name} is working on {self.project_assigned}")