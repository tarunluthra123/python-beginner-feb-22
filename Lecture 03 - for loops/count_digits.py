n = int(input())

# Initialisation
counter = 0


# while n != 0:
while n > 0:
    n = n // 10 # n//=10.     -> update 
    counter += 1 # counter = counter + 1  -> work

print(counter)
