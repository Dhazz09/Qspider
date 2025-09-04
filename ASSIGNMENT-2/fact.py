n=int(input("Enter the number:"))
org=n
final=0
def fact(n):
    f=1
    while n>0:
        f=f*n
        n-=1
    return f
count=0
while org>0:
    count=org%10
    final+=fact(count)
    org//=10
if(final==n):
    print(f"{final} is a strong number")
else:
    print(f"{final}is not a strong number")
    
    