def find_length(s):
    count = 0
    for l in s:
        count += 1
    return count
t=(1,2,3,4,5,6,7,8,9,10)
length = find_length(t)
print(f"Length of the tuple: {length}")