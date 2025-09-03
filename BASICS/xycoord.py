x=int(input("Enter the x coordintes:"))
y=int(input("Enter thee y coordinate:"))
if(x>0 and y>0):
    print("Lies in first quadrant")
elif(x<0 and y>0):
    print("Lies in second quadrant")
elif(x<0 and y<0):
    print("Lies in third quadrant")
else:
    print("Lies in fourth quadrant")