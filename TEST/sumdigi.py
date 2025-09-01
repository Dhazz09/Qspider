a=int(input("Enter the number:"))
count=0
r=0
while(a>0):
    r=a%10
    count+=r
    a//=10
print(count)