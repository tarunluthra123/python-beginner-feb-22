n = 20


# Repeatedly divide by 2 until you get a 0

result = ""

while n > 0:
    rem = n % 2
    # rem is an int
    result = str(rem) + result
    n = n // 2

print(result)
