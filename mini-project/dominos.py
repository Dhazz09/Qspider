import random
class Dominos():
    menu={'veg':{'marghareita':129,'cheese_and_corn':149,'peppi_paneer':179,'loaded_veg':199},
          'non_veg':{'mini_chick':149,'non_veg_loaded':169,'chicken_loaded':200,'mixed_nonveg':220},
          'dessert':{'cheese_cake':130,'moose_cake':145,'brownie':170},
          'snack':{'cheese_balls':110,'chick_ball':130},
          'drink':{'corona_extra':100,'pepsi':50},
          'add_ons':{'extra_cheese':25,'extra_toppings':50,'extra_thin_crust':20,'olive':30,'sauce_pack':30}}
    def __init__(self,name,phno,email):
        self.name=name
        self.phno=phno
        self.email=email
        self.login_status=False
        self.cart={}

        while True:
            if not(self.login_status):
                print("Login")
                ch=input("Do you want to login(y/n):").lower()
                if ch=='y':
                   self.login()
                else:
                   print("In order to proceed further you must login")
            if self.login_status:
                print('-'*50)
                print('-'*10+"Welcome to DOMINO's app 🍕"+'-'*10)
                print("Enter 1 to ORDER")         
                print("Enter 2 to SHOW THE CART")
                print("Enter 3 to logout")
                ch=int(input("Enter your choice:"))
                if ch==1:
                    self.order()
                if ch==2:
                    self.showcart()
                if ch==3:
                    self.logout()            
                else:
                    print("Invalid choice")
    def order(self):
        while True:
            print("MENU"+'>'*5)
            for cat in Dominos.menu:
                print(cat)
            cat=input("Enter the category:")
            if cat in Dominos.menu:
                for item in Dominos.menu[cat]:
                    print(f"{item}..................₹{Dominos.menu[cat][item]}")
                item=input("Enter the item name:")
                if item in Dominos.menu[cat]:
                    q=int(input("Enter the quantity:"))
                    price=q*Dominos.menu[cat][item]
                if item in self.cart:
                    self.cart[item]+=price
                else:
                    self.cart[item]=price
                print(f"{item} is added to the cart")
                ch=input("Do you want to continue to order?(y/n):").lower()
                if ch=='n':
                    break
                else:
                    print(f"{item} not found")
            else:
                print(f"{cat} is not found")
    def login(self):
        print("Login via phone number-1")
        print("Login via email-2")
        pt=int(input("Enter your login type credential:"))
        if pt==1:
            phno=int(input("Enter your phone number:"))
            if phno==self.phno:
                t=self.validate_otp(phno)
                self.login_status=t
                print("LOGIN SUCCESSFUL✅")
            else:
                print("Enter the legitimate number")
        if pt==2:
            email=int("Enter the your mail-id:")
            if '@gmail.com' not in email and email.islower()==False and email!=self.email:
                print("Enter the legitimate mail-id")
            else:
                t=self.validate_otp(email)
                self.login_status=t
                print("LOGIN SUCCESSFUL✅")
    def showcart(self):
        print('<'*5+"DOMINO's CART"+'>'*5)
        if self.cart!={}:
            total=0
            for item in self.cart:
                price=self.cart[item]
                total+=price
                print(f"{item}........₹{price}")
            print("Total price:₹ ",total)
            ch=input("Wamt to place an order?(y/n):").lower()
            if ch=='y':
                print("Thamk you for placing the order")
                print("Your order will deliver soon")
                self.cart={}
            else:
                print("Your cart is empty")
    def logout(self):
        ch=input("Do you really want to log out?(y/n):").lower()
        if ch==y:
            self.login_status=False
        print("You logged out of your account,Thank you for using our app")
    @staticmethod
    def validate_otp(value):
        while True:
            og_otp=random.randint(1000,9999)
            print(f"An OTP has been sent to {value}")
            print(f"OTP:{og_otp}")
            otp=int(input("Enter the OTP:"))
            if otp==og_otp:
                print("Login Successfully✅")
                return True
            print("Invalid OTP,Try again")


ob=Dominos("Dhazz",8015204589,"dhazz09@gmail.com")