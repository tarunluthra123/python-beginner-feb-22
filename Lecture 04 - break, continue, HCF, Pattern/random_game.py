import random

# infinite loop
while True:
    x = random.randint(1, 10)
    if x % 4 == 0:
        continue
    if x == 5:
        break
    print(x, end=' ')
    