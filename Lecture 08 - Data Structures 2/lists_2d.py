a = [[10, 20, 30], [40, 50, 60], [70, 80, 90, 1000], [100, 110, 120]]


for row in a:
    print(*row)

noOfRows = len(a)

# i -> 0 to len(a)-1 -> range(len(a))
for i in range(noOfRows):
    # i loop will run over the indices of the rows
    # a[i] = current row
    # j -> 0 to length of row - 1  -> range(len(a[i]))
    for j in range(len(a[i])):
        # j loop will run over the indices of the columns
        # a[i][j] = current element
        print(i, j, "=>", a[i][j])
