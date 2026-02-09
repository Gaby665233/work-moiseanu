from employee import Employee
class MarketingManager(Employee):
    def __init__(self, name, email, campaign_budget):
        super().__init__(name, email)
        self.campaign_budget = campaign_budget

    def send_email(self, subject, message):
        super().send_email(subject, message)
        print(f"Campaign budget: {self.campaign_budget}")

    def run_campaign(self):
        print(f"{self.name} is running a campaign with a budget of {self.campaign_budget}")