d = {
    "India": "INR",
    5: "ok",
    9.1: "ok",
    True: "ok",
    (2, 7, 1): "ok",
    # [1, 2, 3]: "ok",         -> Error
    # set([1, 2, 3]): "ok",    -> Error
    # {"USA": "USD"}: "ok",    -> Error
}

# print(d)

reverse_currency = {
    "INR": "India",
    "USD": "USA",
    "Ruble": "Russia",
    "Euro": set(("Italy", "Spain")),
    None: "ok",
}

print(reverse_currency)
