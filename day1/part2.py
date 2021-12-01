prev = -1
larger_count = 0
windows_size = 3

with open("input", "r") as f:
    nums = [int(num) for num in f.readlines()]
    for i, val in enumerate(nums):
        if i + windows_size == len(nums):
            break

        val = sum(nums[i : i + windows_size])
        if prev < val:
            larger_count += 1
        prev = val

print(larger_count)
