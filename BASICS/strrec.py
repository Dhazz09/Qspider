def rev(str):
    print(str[::-1])
a=input("Enter a string:")
b=rev(a)
if b==a:
    print("Palindrome:True")
else:
    print("Palindrome:False")