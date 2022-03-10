a = [[10, 20, 30], [40, 50, 60]]
a_rows = len(a)
a_cols = len(a[0])

# To generate the transpose of 'a'

b_rows = a_cols
b_cols = a_rows

b = []

for i in range(b_rows):
    row = []
    for j in range(b_cols):
        row.append(a[j][i])
    b.append(row)

print(b)
