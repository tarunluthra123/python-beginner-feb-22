a = [i**2 for i in range(1, 11)]
print(a)


b = []
for i in range(1, 11):
    b.append(i**2)

print(b)


# Generating square list of all even numbers from 1 to 10
# 2,4,6,8,10
c = [i**2 for i in range(1, 11) if i % 2 == 0]

print(c)

d = []
for i in range(1, 11):
    if i % 2 == 0:
        d.append(i**2)

print(d)
