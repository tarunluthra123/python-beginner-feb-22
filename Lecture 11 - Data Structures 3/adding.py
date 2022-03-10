s = set()


s.add(5)
s.add(10)
s.add(1)
s.add("hello")

l = [8, 9, 1, 0, 4]

# I want to add every element from the list to the set
# for item in l:
#     s.add(item)

s.update(l)
s.update({0, 4, 2})

# List inside set - not allowed
# s.add(l)
# Set inside set - not allowed
# s.add({8, 9, 1})

print(s)
