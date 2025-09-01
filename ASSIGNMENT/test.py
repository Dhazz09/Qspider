#CREATE A FUNCTION TO CHECK WHETHER THE GIVEN NUMBER IS PRIME OR NOT
n=int(input("Enter the number:"))
flag=True 
if(n%2==0):
    flag=False
if(n%n==1):
    flag=False
if flag==True:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")