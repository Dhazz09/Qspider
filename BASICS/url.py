s = ["jiocinema.com", "file.py", "web.html", "amazom.com", "www.org"]
b=[]
for i in s:
    if("com" in i ):
        b.append("com")
    elif("py" in i):
        b.append("py")
    elif("html" in i):
        b.append("html")
    else:
        b.append("org")
print(list(set(b)))

#or[
b=[i.split('.')[-1] for i in s ]
print(list(set(b)))

##sept 07
out=[]
for i in s:
    r=i.split('.')
    if r[-1] not in out:
        out.append(r[-1])
print(f"out{out}")