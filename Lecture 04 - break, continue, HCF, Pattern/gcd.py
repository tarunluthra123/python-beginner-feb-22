a = 20
b = 30

ans = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        # i is a common factor
        # print(i)
        ans = i

print("GCD is", ans)
print(i)
