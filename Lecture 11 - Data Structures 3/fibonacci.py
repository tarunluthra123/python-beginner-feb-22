def fibo(A):
    n = A
    MOD = 10**9 + 7
    first, second = 0, 1
    if n == 1:
        return first
    elif n == 2:
        return second
    else:
        for i in range(n - 1):
            nextVal = (first + second) % MOD
            first = second
            second = nextVal
        return first


print(fibo(100000))
