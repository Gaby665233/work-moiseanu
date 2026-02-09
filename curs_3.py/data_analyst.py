from employee import Employee
class DataAnalyst(Employee):
    def __init__(self, name, email,analysis_tool):
        super().__init__(name, email)
        self.analysis_tool = analysis_tool
    
    def analyze_data(self):
        print(f"{self.name} is analyzing data using {self.analysis_tool}")