class College:
    clgname="PANIMALAR ENGINEERING COLLEGE"   #generic properties
    loc="Chennai"
    @classmethod
    def show(cls):    #cls is classvar
        print(cls.clgname,cls.loc)
    def mod(cls,new):
        cls.loc=new
    def mod1(cls,new2):
        cls.clgname=new2
    def pri(cls):
        print(cls.clgname,cls.loc)
st1=College()
#College.show()
print("Before modificion")
st1.show()
print("AFter modification")
st1.mod("Pune")
st1.pri()
st1.mod1("VIT")
st1.pri()