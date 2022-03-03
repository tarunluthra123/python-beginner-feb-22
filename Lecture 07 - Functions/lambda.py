def square(x):
    return x * x



# Lambda functions
# Lambda functions are a way to create functions without a name.
# Only use lambda functions when you have one line returns


square2 = lambda num: num * num

print(square(10))
print(square2(10))



def getFirst2(a):
    return a[0]


getFirst = lambda a: a[0]

print(getFirst([10, 20, 30, 40]))