n = 5


for i in range(1, n+1):
    # print("*"*i)
    for j in range(1, i+1):
        print("*", end="")
        if i!=j:
            print(" ",end="")
    print("")