import re

with open("D6.txt", "r") as file:
    groups = [group.split("\n") for group in file.read().split("\n\n")]

count = 0

for group in groups:
    groupset = []
    totalgroupset = set()
    
    for passenger in group:
        passengerset = set()
        for letter in passenger:
            totalgroupset.add(letter)
            passengerset.add(letter)
        groupset.append(passengerset)

    for answerset in groupset:
        totalgroupset = totalgroupset & answerset

    count += len(totalgroupset)

print(count)
