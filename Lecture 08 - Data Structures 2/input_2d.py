r, c = map(int, input().split())


a = []


# To read and append 'r' no of rows

for i in range(r):
    row = list(map(int, input().split()))
    a.append(row)


print(a)


# 4 2
# 10 20
# 30 40
# 50 60
# 70 80
