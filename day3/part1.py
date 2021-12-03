counts = []
with open("input", "r") as f:
    for line in f:
        for i, val in enumerate(line.strip()):
            if len(counts) < i + 1:
                counts.append(0)
            if val == "1":
                counts[i] += 1
            else:
                counts[i] -= 1

gamma_rate = ["1" if c > 0 else "0" for c in counts]
epsilion_rate = ["1" if b == "0" else "0" for b in gamma_rate]

gamma_rate = int(f"0b{''.join(gamma_rate)}", 2)
epsilion_rate = int(f"0b{''.join(epsilion_rate)}", 2)
print(gamma_rate * epsilion_rate)
