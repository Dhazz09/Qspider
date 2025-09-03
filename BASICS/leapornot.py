a=int(input("Enter a year:"))
if(a%4==0 and a%400!=0):
    print("It's a leap year")
else:
    print("It's not a leap year")