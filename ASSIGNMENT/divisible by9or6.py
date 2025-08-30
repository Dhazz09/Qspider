#Write a program to print the cube of a number only if the cube is divisible by 9 or 6
a=int(input("Enter the value:"))
b=pow(a,3)
if(b/6==0 or b/9==0):
    print(f"The values {b} is divisible by 6 or 9")
else:
    print(f"The value {b} is not divisible by 6 or 9")