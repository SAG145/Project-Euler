import math

def gcd(x,y):
    while x % y != 0:
        a = x
        b = y
        y = a % b
        x = b
    return y

def m(y,l):
    x = math.isqrt(l - y**2)
    while x % 2 == y % 2 or gcd(x,y) != 1:
        x -= 1
    return y*(x - y)

def bmy(y,l):
    return y*(math.sqrt(l - y**2) - y)

def soly(l):
    my = math.sqrt(l // 2)
    y = 0
    for pow in range(9,-2,-1):
        res = []
        for d in range(10):
            ny = y + d*10**pow
            if ny <= my:
                res.append(bmy(ny,l))
            else:
                res.append(0)
        d = res.index(max(res))
        y += d*10**pow
    return round(y)

def F(R):
    sy = soly(2*R)
    res = []
    for i in range(-10000,10000):
        if sy + i > 0 and 2*(sy + i)**2 < 2*R:
            res.append(m(sy + i,2*R))
    return max(res)

print(F(10**18))

#Answer = 414213562371805310