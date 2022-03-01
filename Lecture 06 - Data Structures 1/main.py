movies = [
    "The Dark Knight",
    "The Shawshank Redemption",
    "The Dark Knight Rises",
    300,
    2.0,
    [
        "The Godfather",
        "The Godfather: Part II",
        "The Godfather: Part III"
    ]
]

# print(movies[1])


movies[2] = "The Lord of the Rings: The Return of the King"
movies[3] = "The Lord of the Rings: The Fellowship of the Ring"
movies[4] = [
    "Harry Potter and the Philosopher's Stone",
    "Harry Potter and the Chamber of Secrets"
]

# print(movies)


movies.append(["Tenet"])

print(movies)


movies.pop()
print(movies)


movies.insert(2, "Spiderman: No Way Home")
print(movies)



if "The Lord of the Rings: Two Towers" in movies:
    print("Yes")
else:
    print("No")


res = "The Lord of the Rings: The Fellowship of the Ring" in movies
print(res)

print(movies.index("The Lord of the Rings: The Fellowship of the Ring"))

print(movies.index("Inception"))
