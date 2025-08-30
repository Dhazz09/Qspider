class College:
     def __init__(cls,cname,loc):
        cls.cname=cname
        cls.loc=loc
    @classmethod
    def disp(cls):
        print(cls.cname,cls.loc)
    def mod(cls,new,new1):
        cls.cname=new
        cls.loc=new1
st1=College("PANIMALR ENGINEERING COLLEGE","PUNE")
print("Before the modification")
st1.disp()
print("After modification")
st1.mod("VIT","PUNE")
st1.disp()