cache = {}

def compute_total(entries, index = 0):
    global cache
    
    if index in cache:
        return cache[index]
    
    if index == len(entries) - 1:
        cache[index] = 1
        return 1
    
    total = sum([compute_total(entries, i) for i, v in enumerate(entries[index+1:index+4], start=index+1) if entries[i] - entries[index] <= 3])

    cache[index] = total
    return total

with open("D10.txt") as file:
    out_joltages = [int(x) for x in file.read().splitlines()]
    
out_joltages.sort()

out_joltages = [0, *out_joltages, out_joltages[-1] + 3]

print(compute_total(out_joltages))
