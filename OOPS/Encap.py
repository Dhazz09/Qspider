class Mobile:
    def __init__(self,brand,battery,pin):
        self.brand=brand
        self._battery=battery   #PROTECTED
        self.__pin=pin          #PRIVATE 
    def get(self):              #GET
        print(self.__pin)
    def set(self,new):          #SET
        self.__pin=new
        print(f"NEW PIN:{self.__pin}")
ob=Mobile("Iphone",100,9211)
print(ob._Mobile__pin)         #ACESSING PRIVATE MEMBERS USING SYNTAX METHOD
ob._Mobile__pin=2007           #MODIFYING PRIVATE MEMBERS USING SYNTAX METHOD
print(ob._Mobile__pin) 
print(ob._battery)
print(ob.brand)
ob.get()
ob.set(1997)