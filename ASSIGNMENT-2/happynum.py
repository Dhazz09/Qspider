n=int(input("Enter the number:"))
org=n
final=set()
count=0
while n!=1 and n not in final:
    final.add(n)
    sumsqr=0
    temp=n
    while temp>0:
        count=temp%10
        sumsqr+=count*count
        temp//=10
    n=sumsqr
if n==1:
    print("Its a happy number")
else:
    print("Its not a happy number")