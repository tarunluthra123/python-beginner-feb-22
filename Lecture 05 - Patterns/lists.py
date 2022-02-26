movies = [
    "The Dark Knight", 
    "The Shawshank Redemption", 
    "The Lord of the Rings: The Return of the King",
    300,
    2.0,
    ["The Godfather",
    "The Godfather: Part II",
    "The Godfather: Part III"],
]

print(movies[5][1])
print(movies)

print(len(movies))
print(len(movies[5]))

# Iterables - range, list, tuple, string, sets, dicts
for movie in movies:
    print(movie)


print(*movies)


# Input for lists of integer numbers
a = list(map(int,input().split()))

print(a)



#  Input for lists of strings
b = input().split()
print(b)
