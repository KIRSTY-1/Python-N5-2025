temperatures = []
for counter in range(0,5):
    temperature = input("Enter temperature:")
    while temperature < -20 or temperature > 50:
        print("Error that is not a valid temperature")
        temperature = int(input("Please enter a valid percentage: "))
    temperatures.append(temperature)
average = (temperatures [1] + temperatures[2] + temperatures[3] + temperatures[4] + temperatures[5])
print(temperatures)
print("your average temperature is:", average, "degrees celcius")


