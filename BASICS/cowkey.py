s={10:"star",20:"bye",30:"moon",40:"apple"}
out={}
#vow=''
for i in s:
    c=''
    for j in s[i]:
        #print(i,j)
        if j in "AaEeIiOoUu":            
            c+=j
    out[i]=c
print(out)