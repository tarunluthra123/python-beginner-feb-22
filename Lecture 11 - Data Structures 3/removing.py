s = {6, 5, 2, 8, 9, 1, 0, "hello", (2, 3)}


# I want to remove 8 from the set
s.remove(8)


# I want to remove num=20 from the set, if it is present
# s.remove(20)  -> giving an error
s.discard(20)

s.discard(9)
s.discard(2)

print(s)
