a=input("Enter the character:")
if(a.isdigit()):
    print(f"{a} is a digit")
elif(a.isalpha()):
    print(f"{a} is a alphabet")
    if(a.isupper()):
        print("and its upper case")
    else:
        print("and its lower case")
elif(not a.isalnum()):
    print(f"{a} is a special character")
else:
    print("Enter valid input")