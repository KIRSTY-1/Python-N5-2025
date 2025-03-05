lengthOfSquarePacks = int(input("Enter the length of square packs being made: "))
specialOffer = input("Is a special offer running? (y/n): ")
additionalRows = int(input("Please enter the number of additional rows included for free: "))

widthOfSquarePacks = lengthOfSquarePacks

if specialOffer == "y":
    totalNumberOfCans = lengthOfSquarePacks * widthOfSquarePacks
    widthOfSquarePacks = widthOfSquarePacks + additionalRows

if lengthOfSquarePacks > 0 and lengthOfSquarePacks < 10:
    totalNumberOfCans = lengthOfSquarePacks * widthOfSquarePacks

print("The number of cans in the pack is: "+str(totalNumberOfCans))