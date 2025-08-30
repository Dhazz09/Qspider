#program to remove duplicate elements from list
a=[1,2,33,42,1,2,1]
b=[]
for i in a:
    if(i not in b):
        b.append(i)
print(b)



c=list(set(a))
print(c)
