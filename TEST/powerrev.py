s="Power star"
words=list(s.split())
dict={}
for i in words:
    dict[i]=i[::-1]
print(dict)
