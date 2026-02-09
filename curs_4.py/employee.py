
# Mini proiect: Extinderea şi suprascrierea metodelor

# Alex doreşte să organizeze informaţiile despre angajaţii din compania sa şi să adauge funcţionalităţi specifice pentru diferite roluri./
#  Să îl ajutăm să facă următoarele:

# Sarcină - Personalizarea claselor pentru roluri specifice în echipă:

# crearea metodei display_info() în clasa Employee care listează numele şi e-mailul angajatului;
# suprascrierea display_info() în clasa SalesManager în aşa fel încât să includă şi obiectivul de vânzări;
# crearea unei clasei noi MarketingManager care:
# moşteneşte Employee;
# adaugă atributul campaign_budget;
# suprascrie metoda send_email() pentru a include informaţii despre bugetul campaniei.
# Instrucţiuni:

# Crearea clasei de bază Employee:
# adăugăm atributele name şi email;
# implementarea metodei send_email() pentru trimiterea mesajelor de e-mail;
# crearea metodei display_info() care listează numele şi e-mailul angajatului.
# Adăugarea specificităţilor pentru SalesManager:
# moştenim Employee;
# adăugăm atributul sales_target;
# suprascriem display_info() pentru includerea obiectivului de vânzări.
# Crearea clasei  MarketingManager:
# moştenim Employee;
# adăugăm atributul campaign_budget;
# suprascriem metoda send_email() în aşa fel încât să includă informaţiile despre bugetul campaniei




class Employee:
    def __init__(self,name,email):
        self.name = name
        self.email = email

    def send_email(self,subject,message):
        print(f"[Employee] Sending email to {self.email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")
    
    def get_role(self):
        return "Employee"
    
    def display_info(self):
        print(f"name {self.name},email: {self.email}")

    