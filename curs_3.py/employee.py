# Mini proiect: Îmbunătăţirea metodelor pentru echipa lui Alex

# Alex conduce o echipă în care fiecare membru are roluri specifice, însă toţi împart sarcinile de bază, precum trimiterea e-mailurilor. /
# Sarcina noastră este să suprascriem metodele conform acestor roluri, pentru ca echipa lui Alex să fie mai eficientă.

# Sarcină – Personalizarea metodei pentru roluri: În primul rând suprascriem metoda send_email() pentru clasele SalesManager şi Intern, /
# în aşa fel încât să listeze următoarele mesaje:

# SalesManager:
# Sending email to alice@brightsales.com
# Subject: Monthly Report
# Message: Please find the attached sales report.
# Sales target for this quarter: 100000
# Alice is tracking sales towards the target of 100000
# DataAnalyst:
# Sending email to bob@brightsales.com
# Subject: Data Analysis
# Message: The data analysis report is ready.
# Bob is analyzing data using Python

# Intern:
# Sending email to charlie@brightsales.com
# Subject: Project Update
# Message: The project is progressing well.
# Project assigned: Market Research
# Charlie is working on Market Research

# Instrucţiuni:

# 1. Clasa de bază Employee:

# Creăm clasa de bază cu atribute comune (name, email) şi metoda send_email(subject, message) care trimite mesaje de e-mail de bază.
# 2. Roluri specifice (SalesManager, DataAnalyst, Intern):

# Moştenim clasa Employee şi adăugăm atribute specifice fiecărui rol (sales_target, analysis_tool, project_assigned).
# Suprascriem metoda send_email() în conformitate cu cerinţele.
# 3. Apelarea funcţiei super():

# În fiecare metodă suprascrisă folosim funcţia super() pentru apelarea implementării de bază send_email() şi adăugarea detaliilor specifice.

class Employee:
    def __init__(self,name,email):
        self.name = name
        self.email = email
    
    def send_email(self,subject, message):
        print(f"sending email to {self.email}")
        print(f"subject: {subject}")
        print(f"Message: {message}")
    

    