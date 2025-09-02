s="abacbaacc"
acount=0
bcount=0
ccount=0
dic={}
for i in s:
    if(i=='a'):
        acount+=1
    elif(i=='b'):
        bcount+=1
    elif(i=='c'):
        ccount+=1
dic['a']=acount
dic['b']=bcount
dic['c']=ccount
print(dic)