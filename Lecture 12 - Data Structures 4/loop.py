currency = {
    "India": "INR",
    "USA": "Dollar",
    "Spain": "Euro",
    "Japan": "Yen",
    "Italy": "Euro",
}


# Iterating over the keys
# for country in currency:
#     print(country, currency[country])

print(currency.items())

for k, v in currency.items():
    print(k, v)
