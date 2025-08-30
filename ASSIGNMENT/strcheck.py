a=input("Enter a value:")
for i in a:
    if(i.isdigit()):
        print(f"{i} is a digit")
    elif(i.isalpha()):
        print(f"{i} is an alphabet")
        if(i.isupper()):
            print("Its an uppercase")
        else:
            print("Its an lower case")
    elif(not i.isalnum()):
        print(f"{i} is a special character")
    else:
        print("Invalid input")

        