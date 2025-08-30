class Bank:
    bname="HARIS BANK"
    bloc="Chennai"
    ifsc_code="HMB9999"
    def __init__(self,cname,pin,cphone,accno,bal):
        self.cname=cname
        self.cphone=cphone
        self.accno=accno
        self.pin=pin
        self.bal=bal
class Atm(Bank):
    def withdraw(self):
        sec=int(input("Enter your pin:"))
        if(sec==self.pin):
            print("PIN is verified.....")
            print("Your selected service is Withdrawl")
            print("1.current account")
            print("2.Savings")
            u=int(input("Select your withdrawl type:"))
            if(u==1):
                amt=int(input("Enter your amount:"))
                print(f"{amt} is dipensed collect it and the withrawl is added to your account" )
            elif(u==2):
                amt=int(input("Enter your amount:"))
                if(amt>self.bal):
                    print("Insufficient balance")
                else:
                    print("The amount is dispensed")
                    print(f"The remaining balance is {self.bal-amt}")
        else:
            print("Invalid pin")    
    def deposit(self):
        sec=int(input("Enter your pin:"))
        if(sec==self.pin):
            print("PIN is verified....")
            print("Your selected serivice is deposit")
            acc=int(input("Enter your account number:"))
            if(self.accno==acc):
                val=int(input("Enter your amount to  be deposited:"))
                self.bal+=val
                print(f"Your new balance is {self.bal}")
            else:
                print("Account not found")
        else:
            print("Invalid pin")
    def balchk(self):
        sec=int(input("Enter the pin:"))
        if(self.pin==sec):
            print(f"Your balance is {self.bal}") 
a=Atm("Dhazz",9211,8015204589,1678,4000)
def operation():
    print("Welcome to HARIS BANK")
    print("Choose the service you want....")
    print("1.DEPOSIT")
    print("2.WITHDRAW")
    print("3.BALANCE QUERY")
    c=int(input("Enter your requiredd service(1/2/3):"))
    if(c==1):
        a.deposit()
    elif(c==2):
        a.withdraw()
    elif(c==3):
        a.balchk()
    else:
        print("Please choose a valid service")
operation()