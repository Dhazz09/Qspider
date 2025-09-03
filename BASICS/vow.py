#Write a python program to check whether the character is vowel or no
a="DHAVasiDharan"
i=0
out=''
while(i<len(a)):
    if a[i] in 'aeiouAEIOU':
        out+=a[i]
    i+=1
print(out)