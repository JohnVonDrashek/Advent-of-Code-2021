from math import prod
from itertools import combinations

with open("D1.txt", "r") as file:
    numbers = [int(line) for line in file.readlines()]

print([prod(c) for c in combinations(numbers, 3) if sum(c) == 2020][0])
