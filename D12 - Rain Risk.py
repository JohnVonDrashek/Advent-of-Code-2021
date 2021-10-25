import re

regex = r"(\w)(\d+)"

with open("D12.txt", "r") as file:
    instructions = [re.findall(regex, line)[0] for line in file.readlines()]

x = 10
y = -1

shipx = 0
shipy = 0

get = {
    "N": lambda x, y, magnitude: (x, y - magnitude),
    "S": lambda x, y, magnitude: (x, y + magnitude),
    "E": lambda x, y, magnitude: (x + magnitude, y),
    "W": lambda x, y, magnitude: (x - magnitude, y)
}

for command, magnitude in instructions:
    magnitude = int(magnitude)
    
    if command == "R":
        for i in range(magnitude//90):  
            tempx = -y
            tempy = x
            x = tempx
            y = tempy
    elif command == "L":
        for i in range(magnitude//90):  
            tempx = y
            tempy = -x
            x = tempx
            y = tempy
    elif command == "F":
        shipx += x*magnitude
        shipy += y*magnitude
    else:
        x, y = get[command](x, y, magnitude)

print(abs(shipx)+abs(shipy))
        
