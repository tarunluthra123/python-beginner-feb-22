book = "Harry Potter and the Half Blood Prince"


idx = book.find("H")
print(idx)

idx = book.find("H", idx + 1)
print(idx)

idx = book.find("H", idx + 1)
print(idx)
