# Toggle Case with While Loop

text = input("Enter a string to toggle: ")
i = 0
toggled = ""
while i < len(text):
    char = text[i]
    if char.islower():
        toggled += char.upper()
    elif char.isupper():
        toggled += char.lower()
    else:
        toggled += char  
    i += 1

print(f"Toggled string: {toggled}")