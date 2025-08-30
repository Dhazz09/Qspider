class College:
    clgname="PANIMALAR ENGINEERING COLLEGE"   #generic properties
    loc="Chennai"
    def __init__(self,name,roll):       #constructor defination
        self.name=name                  #specific properties
        self.roll=roll
    def disp(self):                     #A method is created inside the class and a self parameter is passed
        print(self.name,self.roll) 
    def ch_roll(self,new):              #Object MEthod2
        self.roll=new     
st1=College("Dhavasi",85)
st2=College("Dharan",15)
print("Before changing:")
st1.disp()
st1.ch_roll(67)
print("After changing:")
st1.disp()