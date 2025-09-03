import random
x=random.randint(0,100)
while True:
    us=int(input("Enter your guess between 0 to 100:"))
    if(0<=us<=100):
        if(us>x):
            print("Guess lesser!!")
        elif(us<x):
            print("Guess higher!!")
        else:
            print("Your guess was correct")
    else:
        print("Enter a number between 0 and 100")