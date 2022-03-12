currency = {
    "India": "INR",
    "USA": "Dollar",
    "Spain": "Euro",
    "Japan": "Yen",
    "Italy": "Euro",
}

print(currency["India"])

# if "Russia" in currency:
#     # print("Russia is in currency")
#     print(currency["Russia"])

# russian_currency = currency["Russia"]
russian_currency = currency.get("Russia")

print(russian_currency)
