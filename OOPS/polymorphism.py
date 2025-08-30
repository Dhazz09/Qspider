#Method overloading happening in python or not
def add(a,b):
    return a+b
#print(add(3,2))
v=add               #Monkey patching
def add(a,b,c):
    return a+b+c
print(add(1,2,3))
print(v(2,2))
