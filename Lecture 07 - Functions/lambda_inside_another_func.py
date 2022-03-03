def sumOfSquares(a,b):
    square = lambda x: x*x

    return square(a) + square(b)


print(sumOfSquares(3,4))


def myfunc(n):
    return lambda a:a*n

fun = myfunc(10)

print(fun(20))