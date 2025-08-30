# Middle Value String Checker (Nested elif edition)


my_list = ["Java", 42, "Python", "MidString", 99]
if len(my_list) % 2 != 0:
    mid_index = len(my_list) // 2
    mid_value = my_list[mid_index]
    if type(mid_value) == str:
        print(f"Middle value is a string: '{mid_value}'")
    elif type(mid_value) == int:
        print("Middle value is an integer. Not printing.")
    elif type(mid_value) == bool:
        print("Middle value is a boolean. Not printing.")
    else:
        print(" Middle value is not a string. Skipping output.")
else:

    print("List has even length. No single middle value.")