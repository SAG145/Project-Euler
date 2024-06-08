import math
single = 0
limit = 50*10**6
lst1 = [0]*(limit + 1)
change = 0
b = 1
while change != 100:
    for a in range(math.ceil(b / 3),math.floor(1/3*(math.sqrt(4*b**2 + 3*limit) - b)) + 1):
        n = 3*a**2 + 2*a*b - b**2
        if lst1[n] == 0:
            single += 1
            change = 0
        elif lst1[n] == 1:
            single -= 1
            change = 0
        lst1[n] += 1
    change += 1
    b += 1
print(single)

#answer = 2544559
#זמן הרצה - 14 דקות
