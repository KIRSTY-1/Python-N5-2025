items = []
cost = []

for counter in range (0,3):
    food = input("What items are you buying?: ")
    price = int(input("What is the price of the items you are buying?: "))

    items.append(food)
    cost.append(price)

    quantity = float(input("what is the quantity of the item you are purchasing?: "))
    print("Number of item puchased is: ",quantity)

    total = sum(cost)

print(items)
print("Your total is £: ", total)




