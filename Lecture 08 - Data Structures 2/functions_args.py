def getAvg(a, b, *args):
    # variable number of arguments
    # *args is a tuple
    print("a=", a)
    print("b=", b)
    total = 0
    for num in args:
        total += num
    return total / len(args)


avg = getAvg(2, 6, 1, 8, 4, 3, 2)

print(avg)
