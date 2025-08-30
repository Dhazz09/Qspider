class Car():
    def cprint(self):
        print("In car")
class Bike(Car):
    def bprint(self):
        print("In bike")
class Heli(Car):
    def hprint(self):
        print("In Helicopter")
class Road(Bike,Heli):
    def rprint(self):
        print("In road")
obj=Road()
obj.bprint()
obj.hprint()
obj.rprint()