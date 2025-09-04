deci=int(input("Enter the decimal number:"))
bina=""
while deci>0:
    r=deci%2
    bina=str(r)+bina
    deci//=2
print("Binary value:",bina)