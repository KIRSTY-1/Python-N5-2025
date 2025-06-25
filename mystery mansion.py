names = ["Entrance hall", "Library", "Kitchen", "Garden"]
description = ["A grand foyer with a crystal chandelier", "Dusty bookshelves stretch from floor to ceiling", "Copper pots hang above an old stone hearth", "Overgrown vines twist around marble statues"]
commands = ["N", "S", "E", "W", "Quit", "Help"]

name = input("What is your name?: ")
print("Welcome to the mystery mansion", name)

print("if you head north, you will reach the entrance hall. if you head east, you will reach the library. if you head south, you will reach the kitchen. if you head west, you will reach the garden.")
direction = input("direction (N/S/E/W/quit/help): ")

if direction != "N" and "S" and "E" and "W":
    print("that is not a valid direction. please try again!")
    direction = input("direction (N/S/E/W/quit/help): ")


if direction == "N":
    print("You have arrived into the entrance hall. to your left is a grandfather clock and to your right is a cracked mirror.")
    direction = input("direction (N/S/E/W/quit/help): ")

if direction == "S":
    print("you have arrived in the library. to your left is an old, spider web cover empty bookcases and to your right are boxes overflowing with creepy books.")
    direction = input("direction (N/S/E/W/quit/help): ")

if direction == "E":
    print("you have now arrived in the kitchen. to your left are crackes and shattered plates ansd glasses and to your right is an old table splattered with blood")
    direction = input("direction (N/S/E/W/quit/help): ")

if direction == "W":
    print("you have now arried in the garden. there are no plants, only dead vines and leaves covering the cracked paving slabs.")
    direction = input("direction (N/S/E/W/quit/help): ")

if direction == "help":
    help = ("what do you need help with?: ")
    print("sorry i cannot help with that issue. please contact Amelia Rosenbaum Macaulay but she may not relpy immediately as it is currently the summer holidays.")
    direction = input("direction (N/S/E/W/quit/help): ")

if direction == "quit":
    print("please press the x.")