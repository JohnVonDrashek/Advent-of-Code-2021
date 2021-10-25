import re

with open("D9.txt") as file:
    lines = [int(line) for line in file.read().splitlines()]

back = len(lines) - 2

for i in range(0, back):
    for j in range(i+1, back):
        if sum(lines[i:j+1]) == lines[-1]:
            sorte = lines[i:j+1]
            sorte.sort() 
            print(sorte[0]+sorte[-1])
