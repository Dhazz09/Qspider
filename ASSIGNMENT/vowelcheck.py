#Write a python program to check whether the character is vowel or no
x=input("Enter a value:")
b=x.tolower()
if(b=='a',b=='e',b=='i',b=='o',b=='u'):
    print(f"{b} is vowel")
else:
    print(f"{b} is not vowel")