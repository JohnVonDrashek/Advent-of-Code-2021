import re
import math

regex = r"(\d+)-(\d+)\s(\w):\s(\w+)"

with open("D3.txt") as file:
    entries = [line for line in file.read().splitlines()]

tries = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    
totals = []

for x, y in tries:
    posx = trees = 0
    for posy in range(0, len(entries), y):
        trees += 1 if entries[posy][posx % len(entries[0])] == '#' else 0
        posx += x

    totals.append(trees)

print(math.prod(totals))
