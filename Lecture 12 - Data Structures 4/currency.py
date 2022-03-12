# currency = dict()
currency = {
    "India": "INR",
    "USA": "Dollar",
    "Spain": "Euro",
    "Japan": "Yen",
    "Italy": "Euro",
}

print(currency)


#  Getting the data
indian_currency = currency["India"]

print(indian_currency)
print(currency["USA"])


# Updating the data
currency["USA"] = "USD"


# Creating new entries
currency["Russia"] = "Ruble"
print(currency)
