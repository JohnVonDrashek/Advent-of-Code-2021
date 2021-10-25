import re

regex = r"(\d+)-(\d+)\s(\w):\s(\w+)"

with open("D2.txt", "r") as file:
    entries = [re.match(regex, line).groups() for line in file.readlines()]

valid_passwords = sum([(password[int(start) - 1] == char) ^ (password[int(end)-1] == char) for start, end, char, password in entries])

print(valid_passwords)
