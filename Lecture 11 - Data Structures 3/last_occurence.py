a = [5, 4, 5, 2]
target = 5


for i in range(len(a) - 1, -1, -1):
    if a[i] == target:
        print(i)
        break
