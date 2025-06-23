English = int(input("mark for English (%): "))
Maths = int(input("mark for Maths (%): "))
Art = int(input("mark for Art (%): "))
Computing = int(input("mark for Computing (%): "))

sum = English + Maths + Art + Computing
average = sum / 4

print("English:", English,"%")
print("Maths:", Maths,"%")
print("Art:", Art,"%")
print("Computing:", Computing,"%")
print("Average Mark:", average,"%")