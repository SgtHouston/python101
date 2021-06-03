# Ask for name
user_name = input("What is your name?: ")

# Greet User
print(f"Hello, {user_name}!")

# Check Length of name
name_length = len(user_name)

# If longer than 10 say, "Wow, long name!"
if name_length > 10:
    print('Wow, long name!')

else:
    print("Cool name, bro!")
    
