# At Least 13 Characters
# Uppercase Letter
# Lowercase Letter
# Number
# Special Character

print("Hello, this is a Password Checker program.")
user_input_password = input("Please enter your password to check its strength: ")

# using if statement to check for length

if user_input_password.__len__() >= 13:
    print("Enough Characters")
else:
    print("Too Short")

# Next Feature would be UpperCase and Lowercase Check

if user_input_password.islower():
    print("No Uppercase Letter")

