a = []

rows = 4
cols = 3


for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i + j)
    a.append(row)

print(a)
