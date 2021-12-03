def find_level(lines, index=0, tie_breaker="1"):
    ones = []
    zeros = []
    for l in lines:
        if l[index] == "1":
            ones.append(l)
        else:
            zeros.append(l)

    if len(lines) == 2 and len(ones) == len(zeros):
        if lines[0][index] == tie_breaker:
            return int(f"0b{lines[0].strip()}", 2)
        else:
            return int(f"0b{lines[1].strip()}", 2)

    if (len(ones) > len(zeros) and tie_breaker == "1") or (
        len(ones) < len(zeros) and tie_breaker == "0"
    ):
        return find_level(ones, index + 1, tie_breaker)
    else:
        return find_level(zeros, index + 1, tie_breaker)


with open("day3/input", "r") as f:
    lines = [l.strip() for l in f.readlines()]

    oxygen_level = find_level(lines)
    scrubber_rating = find_level(lines, tie_breaker="0")

    print(oxygen_level)
    print(scrubber_rating)
    print(oxygen_level * scrubber_rating)
