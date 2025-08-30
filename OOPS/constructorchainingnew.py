class A:
    a=100
    def __init__(self,b,c):
        self.b=b
        self.c=c
    def display(self):
        print(self.b,self.c)
    def ch_add(self,new):
        self.b=new
class B(A):
    v=97
    def __init__(self,x,y,a,b):    #Constructor chaining 
        super().__init__(a,b)
        self.x=x
        self.y=y
    def display(self):
        super().display()           #method chaining
        print(self.x,self.y)
    def ch_add_name(self,new_a,new_b):
        super().ch_add(new_b)
        self.a=new_a
        print(self.a,self.b)
obj1=B(10,20,30,40)
obj1.display()
obj1.ch_add_name(23,24)
#Method overriding
