s="bacbcaabbaa"
acount=0
bcount=0
ccount=0
for i in s:
    if(i=='a'):
        acount+=1
    elif(i=='b'):
        bcount+=1
    elif(i=='c'):
        ccount+=1
print(f"b{bcount}a{acount}c{ccount}")