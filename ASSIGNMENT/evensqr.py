#Way to print the square of a number only if its even
a=int(input("Enter the value:"))
x=pow(a,2)
if(x/2==0):
    print(f"{x} is squared and divisible by 2")
else:
    print(f"{x} is squared but not divisible by 2")