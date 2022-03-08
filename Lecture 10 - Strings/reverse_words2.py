s = "Hello World"
# Result = olleH dlroW


words = s.split()

print(words)


for i in range(len(words)):
    # words[i] = "".join(reversed(words[i]))
    words[i] = words[i][::-1]


print(words)
# result = " ".join(words)

# print(result)
