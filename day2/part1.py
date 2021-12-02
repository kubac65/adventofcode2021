distance = 0
depth = 0

with open("input", "r") as f:
    for line in f:
        direction, value = line.strip().split(" ")
        if direction == "down":
            depth += int(value)
            continue
        if direction == "up":
            depth -= int(value)
            continue
        if direction == "forward":
            distance += int(value)

print(distance * depth)
