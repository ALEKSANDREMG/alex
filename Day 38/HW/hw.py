user_input = input("Please enter a string: ")

if user_input.islower():
    print("The string contains only lowercase letters.")
elif user_input.isupper():
    print("The string contains only uppercase letters.")
else:
    print("The string does not contain only lowercase letters. It contains both.")
