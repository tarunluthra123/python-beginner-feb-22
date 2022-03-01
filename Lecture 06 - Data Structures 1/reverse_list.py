a = [10,20,30,40,50]

# Reverse the list without using inbuilt function
# b = [50,40,30,20,10]

# a should remain intact
# b should contain its reverse

# a.reverse()

b = []

for i in range(len(a)-1,-1,-1):
    b.append(a[i])

print(b)