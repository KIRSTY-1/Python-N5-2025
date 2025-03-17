home = 0
away = 0 
period = 1 

while period <= 3:
    #print score and period
    print("------------------")
    print("home -",home,"-",away,"- away")
    print("period",period)
    print("------------------")
    print()
    option = input("Enter (h)ome, (a)away or (x) to end period: ")
    while option != "h" and option != "a" and option != "p":
        print("this is not an option. please try again!")
        option = input("enter (h)ome, (a)way or (p) to end a period: ")
        if option == "p":
            period == period + 1
        if option == "h":
            h = h + 1
        if option == "a":
            a = a + 1
