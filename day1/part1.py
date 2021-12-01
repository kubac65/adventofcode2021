prev = None
larger_count = 0
with open("input", "r") as f:
    for line in f:
        num = int(line)
        if prev is None:
            prev = num
            continue

        if prev < num:
            larger_count += 1
        prev = num

print(larger_count)
