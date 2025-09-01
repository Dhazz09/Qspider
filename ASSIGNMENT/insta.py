# Insta Login Simulator (Nested if-else edition)

# Predefined valid credentials
valid_username = "dhazz_insta"
valid_password = "pass123"
username = input("Enter your Instagram username: ")
if username == valid_username:
    print(" Username is valid. Proceeding to password...")
    password = input("Enter your password: ")
    if password == valid_password:
        print("Login successful! Welcome to the 'Gram.")
    else:
        print(" Incorrect password. Try again or reset.")
else:

    print(" Invalid username. Access denied.")