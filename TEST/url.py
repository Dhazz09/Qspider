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

