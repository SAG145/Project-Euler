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

def S(n,mod):
    t = pow(2,n - 1,mod)
    s = -math.isqrt(n)*(t - pow(2,n - n // math.isqrt(n),mod))
    for d in range(1,math.isqrt(n) + 1):
        s += d*(t - pow(2,n - n // d,mod))
        s += sum_range(n // (d + 1) + 1,n // d)*(t - pow(2,n - d,mod))
        s %= mod
    return s

print(S(10**14,1234567891))

#Answer = 1228599511

#Time: 2:00