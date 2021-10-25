import copy
import itertools

with open("D11.txt", "r") as file:
    rows = [[char for char in line.strip('\n')] for line in file.readlines()]

def crawl(x, y, i, j):
    while True:
        x += i
        y += j

        if not (0 <= x < len(rows) and 0 <= y < len(rows[0])): break

        if rows[x][y] == "#": return True
        if rows[x][y] == "L": return False

    return False

doloop = True
count = 0

while doloop:
    change = {}
    
    for x, row in enumerate(rows):
        for y, val in enumerate(row):
            if val == ".": continue
            
            occupied = []

            for i in range(-1,2):
                for j in range(-1,2):
                    if not i == j == 0: occupied.append(crawl(x,y,i,j))

            if val == "L" and not any(occupied): change[x,y] = "#"
            if val == "#" and sum(occupied) >= 5: change[x,y] = "L"
                    
    for x, y in change: rows[x][y] = change[x,y]

    if len(change) == 0: doloop = False

count = 0

for x, row in enumerate(rows):
    for y, val in enumerate(row):
        if val == "#":
            count += 1

print(count)



