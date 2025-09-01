a=int(input("Enter the number:"))
l=len(str(a))
tot=0
r=0
didi=0
while(a>0):
    didi=a%10
    tot+=didi**l
    a//=10
print(tot)