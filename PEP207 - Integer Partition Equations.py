import math

perfect = 1
partitions = 1
x = 2
while perfect / partitions >= 1/12345:
    k = x**2 + x
    s = (1 + math.sqrt(4*k + 1)) / 2
    t = math.log(s,2)
    if math.floor(t) == t:
        perfect += 1
    partitions += 1
    x += 1
print(k)

#Answer = 44043947822

