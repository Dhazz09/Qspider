#states of the properties
class College:
    clgname="PANIMALAR ENGINEERING COLLEGE"   #generic properties
    loc="Chennai"
    def __init__(self,name,roll):       #constructor defination
        self.name=name                  #specific properties
        self.roll=roll
st1=College("Dhavasi",85)
st2=College("Dharan",15)
#st1.name="Dhavasi"
#st1.roll="85"
#st2=College()
#st2.name="Dharan"
#st2.roll="15"
print(st1.clgname)
print(st1.name)
print(st1.roll)
print(st2.clgname)
print(st2.name)
print(st2.roll)
