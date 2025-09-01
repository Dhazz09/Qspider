class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):              #funtion passing
        return self.a+other.a
    def __sub__(self,other):
        #return self.a-other.a
        print("Dhazz")
    def __mul__(self,other):
        return self.a*other.a
    def __truediv__(self,other):
        return self.a/other.a
obj=A(20)
ob1=A(50)
print(obj+ob1)
print(obj-ob1)
print(obj*ob1)
print(obj/ob1)