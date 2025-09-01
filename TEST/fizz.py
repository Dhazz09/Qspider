a=int(input("Enter a number:"))
if(a%3==0 and a%5!=0):
    print("Fizz")
elif(a%5==0 and a%3!=0):
    print("buzz")
elif(a%3==0 and a%5==0):
    print("Fizzbuzz")
else:
    print("Ente a number which is a multiple of 3 or 5 or both")