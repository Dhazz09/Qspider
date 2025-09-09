s="always keep smiling"
a=s.split()
p=""
for i in a:
    p+=" "+(i[::-1])
print(p)



OUT=[]
for i in s.split():
    OUT+=[i[::-1]]
print(' '.join(OUT))