s = "Python is amazing and awesome"


words = s.split()


# words = words[::-1]
# words = list(reversed(words))
words.reverse()

# words = ['awesome', 'and', 'amazing', 'is', 'Python']
# words is a list of str


result = " ".join(words)
print(result)

# print(words)
