import random
x=random.randint(0,6)
while True:
    us=int(input("Roll your dice:"))
    if(0<=us<=6):
        if(us>x):
            print("YOU WONNN!!")
            break;
        elif(us<x):
            print("YOU LOSE!!")
        else:
            print("TIE") 
    else:
        print("ROLL CORRECTLY")