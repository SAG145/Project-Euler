import math
n = 64*10**6
lst = [1]*n
for k in range(2,n // 2 + 1):
    i = k
    p = k**2
    while i < n:
        lst[i] += p
        i += k

for j in range(n // 2 + 1,n):
    lst[j] += j**2

s = 0
for i in range(1,len(lst)):
    ssd = lst[i]
    if math.isqrt(ssd)**2 == ssd:
        s += i

print(s)

#answer = 1922364685
#זמן הרצה - 28 דקןת