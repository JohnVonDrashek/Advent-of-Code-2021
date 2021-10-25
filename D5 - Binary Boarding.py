translator = str.maketrans("FBLR", "0101")

taken = set(int(ticket.translate(translator), 2) for ticket in open("D5.txt").read().splitlines())

low, high = min(taken), max(taken)

print(high)
print(next(seat for seat in range(low + 1, high) if seat not in taken))
