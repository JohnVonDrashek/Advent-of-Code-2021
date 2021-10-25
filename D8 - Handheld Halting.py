with open("D8.txt") as file:
    instructions = [line.split(' ') for line in file.read().splitlines()]

flip = {"jmp":"nop","nop":"jmp","acc":"acc"}

for i, inst in enumerate(instructions):
    acc, line, passed = 0, 0, set()
    
    while line not in passed:
        passed.add(line)
        op, val = instructions[line]

        if line == i: op = flip[op]
        
        if op == "acc":
            acc += int(val)
            line += 1
        elif op == "jmp": line += int(val)
        elif op == "nop": line += 1
        
        if line >= len(instructions):
            print(acc)
            break

    
    
