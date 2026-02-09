from sales_manager_with_display import SalesManager
from marketing_manager import MarketingManager


alice = SalesManager("Alice", "alice@brightsales.com", 100000)
bob = MarketingManager("Bob", "bob@marketing.com", 50000)

print("SalesManager:")

alice.display_info()
alice.send_email("Monthly Report", "Please find the attached sales report.")
alice.track_sales()


print("\nMarketingManager:")

bob.display_info()
bob.send_email("Campaign Update", "The new campaign is live!")
bob.run_campaign()
