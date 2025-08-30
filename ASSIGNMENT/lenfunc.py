#program to find the lenght of the string without len()
def find_length(s):
    count = 0
    for _ in s:
        count += 1
    return count
text = input("Enter a string: ")
length = find_length(text)

print(f" Length of the string: {length}")