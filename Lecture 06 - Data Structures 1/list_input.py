# 10 20 30 40
a = input()
# a is a string
# a = "10 20 30 40"


b = a.split()
# b is a list
# b = ['10', '20', '30', '40']


for i in range(len(b)):
    b[i] = int(b[i])


print(b)
print(type(b))
print(b[0])
print(type(b[0]))