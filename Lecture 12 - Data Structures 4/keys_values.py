currency = {
    "India": "INR",
    "USA": "Dollar",
    "Spain": "Euro",
    "Japan": "Yen",
    "Italy": "Euro",
}


#  Get the keys of currency dict
countries = currency.keys()

print(countries)
print(type(countries))

for country in countries:
    print(country)


# Get the values of currency dict
currencies = currency.values()

for c in currencies:
    print(c)
