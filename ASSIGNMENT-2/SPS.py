import random
c=["stone","paper","scissor"];
while True:
        #while(i<=5):
    user=input("Enter your choice(stone,paper,scissor or exit)\n")
    #print("*******************************")
    if(user=="exit"):
        print("Game is ending")
        print("----")
        break
    elif(user not in c):
        print("Enter valid input")
        #print("********************")
        continue
    print(f"Your choice: {user}")
    #print("**********************")
    comp=random.choice(c)
    print(f"computer's choice: {comp}")
    #print("***************************")
    if((user=="stone" and comp=="stone")or(user=="scissor" and comp=="scissor")or(user=="paper" and comp=="paper")):
        print("It's draw buddy");
        print("-------")
    elif((user=="stone" and comp=="scissor")or(user=="paper" and comp=="stone" )or(user=="scissor" and comp=="stone")):
        print("YOU won")
        print("<<<>>>>")
        break
    else:
        print("You lose")
        print("-------")
    