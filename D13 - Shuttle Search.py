import math

with open("D13.txt") as file:
    schedules = [(i, int(time)) for i, time in enumerate(file.read().splitlines()[1].split(',')) if time != 'x']

jump, timestamp, biggest, prev = 1, 0, 0, []

while biggest != len(schedules):
    timestamp += jump

    count = sum([(timestamp + i) % time == 0 for i, time in schedules])

    if len(prev) == 1 and count == biggest:
        jump = max(jump, timestamp - prev.pop())
    if count > biggest:
        biggest = count
        prev = [timestamp]

print(timestamp)
