a=input("Enter a string:")
if(a.isupper()):
    print("Its uppercase")
elif(a.islower()):
    print("Its lowercase")
elif(a.isdigit()):
    print("Its a digit")
else:
    print("Its a special character")