import math

def an(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2*an(n // 2)
    return an(n // 2) - 3*an(n // 2 + 1)

def S(n):
    s = 0
    m = 1
    while m < n:
        if 3*m < n:
            s -= 5*m
        s += m
        q = n // m
        if q % 4 == 1 or q % 4 == 2:
            if 2**round(math.log(q - 1 + q % 2,2)) != q - 1 + q % 2:
                s += m * an(q - 1 + q % 2)
        m *= 2
    return s

print(S(10**12))

#Answer = -6999033352333308
