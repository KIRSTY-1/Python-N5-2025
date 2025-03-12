number_of_badges = int(input("Please enter the number of badges you would like to order: "))

if number_of_badges > 150:
    total_cost = number_of_badges*0.25*0.9
    print("your total cost including discount is: ")


else:
    total_cost = number_of_badges*0.25
    print("Yout total cost is: ")