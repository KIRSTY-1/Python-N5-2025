pricepermile = 0
startMiles = 0
for index in range (1,5):
    currentmiles = int(input("What is your current mileage?: "))
    rating = int(input("What is your valid kW at your current charging station?: "))
    while rating != 7 and rating != 22 and rating != 50:
        print("Error...")
        rating = int(input("What is your valid kW at your current charging station?: "))    
   
    if rating == 7:
        pricepermile = 0
    elif rating == 22:
        pricepermile = 0.005
    else:
        pricepermile = 0.01

    milestraveled = currentmiles - startMiles
    startMiles = currentmiles

    cost = pricepermile * milestraveled 
    print("the cost of this stage is: £", cost)


    

