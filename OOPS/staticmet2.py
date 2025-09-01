class LoginForm:
    def __init__(self,name,roll,phno,email):
        self.name=name
        self.roll=roll
        self.phno=phno
        self.email=email
    @staticmethod
    def valid_phno(phno):
        s=str(phno)
        if len(s)==10 and '6'<=s[0]<='9':
            return True
        else:
            return False
    @staticmethod
    def valid_email(email):
        if "@" in email and "." in email:
            return True
        else:
            return False
    def display(self):
        if self.valid_email(self.email) and self.valid_phno(self.phno):
            print(self.name,self.roll,self.email,self.phno)
        else:
            print("invalid email or phno")
ob1=LoginForm("Bharat",201,6234567890,"bharat@gmail.com")
ob1.display()