a="100111001"
b="000111011"
i=0
count=0
while i<len(a):
    if a[i]==b[i]:
        count+=1
    i+=1
print(count)