a = [2, 1, 3, 2, 5, 2, 3, 6]

freq = {}

for num in a:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)

maxFreq = max(freq.values())
print(maxFreq)

maxKey = None


for key, value in freq.items():
    if value == maxFreq:
        maxKey = key
        break

print(maxKey)
