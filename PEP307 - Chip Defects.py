from math import factorial

def p(k,n):
    s = 0
    f = factorial(k)
    p = factorial(n) // factorial(k // 2) // factorial(k % 2) // factorial(n - k // 2 - k % 2)
    for twos in range(k // 2,-1,-1):
        ones = k - 2*twos
        s += p*f // 2**twos
        p = p*twos*(n - ones - twos) // ((ones + 1)*(ones + 2))
    return 1 - s / n**k

print(round(p(20000,1000000),10))

#Answer = 0.7311720251

#Time: 2:00