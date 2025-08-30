class Bank:
    def display(self):
        print("you are in the bank")
class Saving_acc(Bank):
    def disp(self):
        print("You are in saving acc")
class Current_acc(Bank):
    def __init__(self,name,add):
        self.name=name
        self.add=add
    def show(self):
        super().display()
        print(self.name,self.add)
obj1=Current_acc('abc','xyz')
obj1.show()
obj2=Saving_acc()
obj2.disp()
