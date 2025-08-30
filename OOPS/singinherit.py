class A:
    def disp():
        print("Hello from A")
    a=90
    b=78
class B(A):
    c=67
    d=A.a+A.b
print(B.a)
B.disp()
print(B.d)
