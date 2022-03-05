continents = (
    "Africa",
    "North America",
    "South America",
    "Asia",
    "Australia",
    "Europe",
    "Antarctica",
)

l = list(continents)

l.sort()


continents = tuple(l)
print(continents)

for continent in continents:
    print(continent)
