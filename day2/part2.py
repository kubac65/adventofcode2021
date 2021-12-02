distance = 0
depth = 0
aim = 0

with open("input", "r") as f:
    for line in f:
        direction, value = line.strip().split(" ")
        if direction == "down":
            aim += int(value)
            continue
        if direction == "up":
            aim -= int(value)
            continue
        if direction == "forward":
            distance += int(value)
            depth += aim * int(value)

print(distance * depth)
