a=input("Enter the sentence:")
b=list(a.split())
for i in b:
    for j in i:
        if(j[0].isupper()):
            print(i)