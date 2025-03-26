name = ["Kirsty", "Amelia", "Emma-Grace"]
mostCharacters = len(name[0])
pos = 0
for index in range(1,len(name)):
    if len(name[index]) > mostCharacters:
        mostCharacters = len(name[index])
        pos = index

print(name[pos], "has the most number of characters", mostCharacters)