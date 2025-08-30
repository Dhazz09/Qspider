class Studies:
    def study(self):
        print("We are genius")
class Fun:
    def act(self):
        print("We are happy")
class Student(Studies,Fun):
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
ob1=Student("Dhavasi",15)
ob1.act()
ob1.study()