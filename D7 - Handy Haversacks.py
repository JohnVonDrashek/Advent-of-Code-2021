import re

with open("D7.txt") as file:
    rules = file.read().splitlines()

rulesdict = {re.findall(r"(\w+ \w+)", rule)[0]:re.findall(r"(\d) (\w+ \w+)", rule) for rule in rules}

def absorb(bag, amount=1):
    return amount + sum([absorb(sub_bag, int(num)) * amount for num, sub_bag in rulesdict[bag]])

print(absorb("shiny gold") - 1)
