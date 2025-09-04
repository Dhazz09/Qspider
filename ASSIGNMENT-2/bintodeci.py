bina=int(input("Enter the binary number:"))
deci=0
powe=0
ininum=0
while bina>0:
    ininum=bina%10
    deci+=ininum*(2**powe)
    bina//=10
    powe+=1
print(f"{bina} decimal's value is {deci}")