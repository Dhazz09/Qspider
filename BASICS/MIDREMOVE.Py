s=["hai",34,3.4,"hello",90,"byebye"]
out={}
for i in s:
    if type(i) not in [int,float]:
        out[i]=i[0]+i[len(i)-1]
print(out)