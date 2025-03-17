# Program 2 - Predict and read
cost = float(input("Enter cost of the item in £ and p: "))
noPounds = int(cost)+1
print("You will need £"+str(noPounds))
print("And you will get "+str(noPounds-cost)+"p change")

# £4
# before the code was fixed £2.50 would give you a negative number of change 