class Resume10:
    def __init__(self,name,add,ten_perc,tpy):
        self.name=name
        self.add=add
        self.ten_perc=ten_perc
        self.tpy=tpy
    def display(self):
        print(self.name,self.add,self.ten_perc,self.tpy)
class Resume12(Resume10):
    def __init__(self,name,add,ten_perc,tpy,twelve_perc,ttpy):
        super().__init__(name,add,ten_perc,tpy)
        self.twelve_perc=twelve_perc
        self.ttpy=ttpy
    def display(self):
        super().display()
        print(self.twelve_perc,self.ttpy)
class Resumebtech(Resume12):
    def __init__(self,name,add,ten_perc,tpy,twelve_perc,ttpy,cgpa,cpy,category):
        super().__init__(name,add,ten_perc,tpy,twelve_perc,ttpy)
        self.cgpa=cgpa
        self.cpy=cpy
        self.category=category
    def display(self):
        super().display()
        print(self.cgpa,self.cpy,self.category)
obj2=Resumebtech("Dhazz","chennai",90,2022,98,2024,8.9,2028,"EEE")
obj2.display()