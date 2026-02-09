from sales_target import SalesManager
from data_analyst import DataAnalyst
from intern import Intern

alice = SalesManager("Alice", "alice@brightsales.com", 100000)
bob = DataAnalyst("Bob", "bob@brightsales.com", "Python")
charlie = Intern("Charlie", "charlie@brightsales.com", "Market Research")


print("SalesManager:")

alice.send_email("Monthly Report","Please find the attached sales report.")
alice.track_salves()

print("\nDataAnalyst:")
bob.send_email(" Data Analysis","The data analysis report is ready.")
bob.analyze_data()

print("\nIntern:")

charlie.send_email("Project Update","The project is progressing well.")
charlie.work_on_project()
