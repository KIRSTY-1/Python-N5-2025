# Program 3 - Investigate and modify
password = input("Please enter your password: ")
while len(password) < 8:
    print("Error, try again.")
    password = input("Please enter your password: ") 
print("Password accepted.")

# it will print an error message
