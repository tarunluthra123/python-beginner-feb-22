# Skip printing the multiples of 5

i = 0
while i <= 100:
    i += 1
    if i % 5 == 0:
        continue
    print(i, end=' ')
    
    
