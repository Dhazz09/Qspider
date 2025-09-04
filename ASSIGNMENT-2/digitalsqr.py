n=int(input("Enter the number:"))
org=n
final=set()
count=0
while n!=1 and n not in final:
    final.add(n)
    digisqr=0
    temp=n
    while temp>0:
        count=temp%10
        digisqr+=count
        temp//=10
    n=digisqr
if 1<=n<=9:
    print(f"{n} a digital square ")
else:
    print(f"{n}is not a digital square  ")