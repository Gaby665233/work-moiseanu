class DataAnalyst:
    def __init__(self, name, email, analysis_tool):
        self.name = name
        self.email = email
        self.analysis_tool = analysis_tool

    def send_email(self, subject, message):
        print(f"Sending email to {self.email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")

    def analyze_data(self):
        print(f"{self.name} is analyzing data using {self.analysis_tool}")