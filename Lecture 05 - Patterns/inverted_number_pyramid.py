n = 8



for i in range(1, n+1):
    # to print (n-i) spaces before printing the number
    # Solution 1: - using the string multiplication
    # print(" "*(n-i), end="")

    # Solution 2: - using loops
    for j in range(n-i):
        print("  ", end="")

    # j-loop prints the numbers in the row
    for j in range(1, i+1):
        print(j,end=' ')

    # new line
    print()