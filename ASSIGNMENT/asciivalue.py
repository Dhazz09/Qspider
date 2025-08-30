#Write a program to print the ASCII value of the character only if its uppercas
char=input("ENter the letter:")
if (len(char) == 1 and char.isupper()):
    print(f"The ASCII value of '{char}' is {ord(char)}")
else:
    print("The character is not uppercase.")



v=input("Enter the value:")
if('A'<=v<='Z'):
    print(ord(v))