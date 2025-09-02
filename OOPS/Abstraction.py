from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def start(self):  #ABSTRACT METHOD
        pass
    @abstractmethod
    def stop(self):
        pass
#ob=Car()
class Electric_car(Car):
    def start(self):
        print("Car is started using battery")
    def stop(self):
        print("Car is stopped")
    def battery(self):
        print("This uses Battery")
class Petrol_car(Car):
    def start(Self):
        print("This car starts using petrol")
    def stop(self):
        print("car stops")
    def petrol(self):
        print("This car uses petrol")
ob=Electric_car()
ob.start()
ob.stop()
ob.battery()
ob1=Petrol_car()
ob1.start()
ob1.stop()
ob1.petrol()
