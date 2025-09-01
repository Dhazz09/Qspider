class Mobile:
    def __init__(self,brand,battery,pin):
        self.brand=brand
        self._battery=battery   #PROTECTED
        self.__pin=pin          #PRIVATE
ob=Mobile("Iphone",100,9211)
#print(ob.__pin)
print(ob._battery)
print(ob.brand)