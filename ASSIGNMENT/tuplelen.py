#  Homogeneous Tuple Length Finder (No len(), using for loop)


my_tuple = (10, 20, 30, 40, 50) 
expected_type = type(my_tuple[0])
count = 0
for item in my_tuple:
    if type(item) == expected_type:
        count += 1
    else:
        break  

print(f"Length of homogeneous tuple: {count}")