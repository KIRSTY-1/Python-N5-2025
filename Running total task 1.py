
total = 0
# Loop 12 times
for index in range(12):
    thismonthssavings = float(input("Enter this month's savings (£): "))
    total = total + thismonthssavings
    print("Your savings so far this year is (£): ", round(total,2))

