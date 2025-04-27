import math

def sum_range(a,b):
    return (b*(b + 1) - a*(a - 1)) // 2

def all_div_sum(n):
    s = 0
    if n // math.isqrt(n) == math.isqrt(n):
        s -= math.isqrt(n)**2
    for i in range(1,math.isqrt(n) + 1):
        s += i*(n // i)
        s += i*sum_range(n // (i + 1) + 1,n // i)
    return s

limit = 10**8

apf = []
for _ in range(math.isqrt(limit) + 1):
    apf.append(set())
for p in range(2,len(apf)):
    if len(apf[p]) == 0:
        for n in range(p,len(apf),p):
            apf[n].add(p)

s = all_div_sum(limit)
for a in range(1,math.isqrt(limit) + 1):
    for b in range(1,min(math.isqrt(limit - a**2),a) + 1):
        if len(apf[a] & apf[b]) == 0:
            t = a**2 + b**2
            r = 2*(a + b)
            if a == b:
                r -= 2*a
            s += r*all_div_sum(limit // t)

print(s)

#Answer = 17971254122360635