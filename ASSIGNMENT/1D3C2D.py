# WAP to check the number of digits in an integer using elif

num = int(input("Enter an integer: "))
num_abs = abs(num)  # Handle negative numbers

if num_abs < 10:
    print("Single digit")
elif num_abs < 100:
    print("Two digits")
elif num_abs < 1000:
    print("Three digits")
else:
    print("More than three digits")