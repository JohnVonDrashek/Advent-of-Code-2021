import re

with open("D14.txt") as file:
    lines = file.read().splitlines()

mem_regex = r"\w+\[(\d+)] = (\d+)"
mask_regex = r"\w+ = (\w+)"

mask = ""
memory = {}

def recurse():
    pass

for line in lines:
    r1 = re.match(mem_regex, line)
    r2 = re.findall(mask_regex, line)

    if r1 != None:
        address, val = r1.groups()
        address = "{0:b}".format(int(address))[::-1]
        result = ""
        
        for i, char in enumerate(reversed(mask)):
            if char == "X" and i < len(val):
                result = val[i] + result
            else:
                result = char + result
        memory[address] = int(result, 2)
    elif r2 != None:
        mask = r2[0]

mysum = 0
for key, val in memory.items():
    mysum += val

print(mysum)
