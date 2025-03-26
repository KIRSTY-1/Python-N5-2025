list = []

age = int(input("Enter your age: "))

while age < 11 or age > 18:
    print("Error! You are not able to enter the talent show!")
    age = int(input("Enter your age: "))
if age >10 or age < 19:
    print("You can enter the talent show!")
    
list.append(age)
print(list)

