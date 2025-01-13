import math
s = 0
for c in str(math.isqrt(10**2010*13))[1:1001]:
    s += int(c)
print(s)

#answer = 4588
