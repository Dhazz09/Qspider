s=["jiocinema.com","file.py","web.html","amazon.com","www.org"]
out={}
for i in s:
    r=i.split('.')
    if r[-1] not in out:
        out[r[-1]]=[r[0]]
            #key    value   
    else:
        out[r[-1]].append(r[0]) 
print(out)

#b=[i.split('.')[-1] for i in s ]
#print(list(set(b)))
