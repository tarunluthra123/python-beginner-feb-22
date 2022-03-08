s = "10100"


# Iterate over this string in reversed order
# Right to left

result = 0
i = 0

for digit in reversed(s):
    value = int(digit) * (2**i)
    result += value
    i += 1

print(result)
