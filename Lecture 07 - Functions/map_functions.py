a = [2, 5, 1, 6, 8, 9]
# Generate a list containing squares of all the numbers in a
# b = [4, 25, 1, 36, 64, 81]


# Function - square
# Iterable - list a

def square(x):
    return x * x


# b = []
# for x in a:
#     b.append(square(x))
# print(b)

b = list(map(square, a))
# map function is faster than the loop solution above
# It is easier to understand and write

print(b)




