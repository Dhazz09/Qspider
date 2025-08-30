a=input("Enter the string:")
for i in a:
    if(not i.isalnum()):
        print(f"{i} is a special character")