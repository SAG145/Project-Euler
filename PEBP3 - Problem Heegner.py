import math
from fractions import Fraction

def recip(t,n):
    a = t[0]
    b = t[1]
    r = a**2*n - b**2
    return (a / r, - b / r)

def cf(n):
    a_list = []
    sqrt1 = math.sqrt(n)
    f1 = Fraction(1,1)
    f2 = Fraction(0,1)
    t = (f1,f2)
    while True:
        a_list.append(math.floor(sqrt1*t[0] + t[1]))
        t = (t[0],t[1] + Fraction(a_list[-1],-1))
        t = recip(t,n)
        if a_list[-1] == 2*math.floor(sqrt1):
            return a_list

def fraction(n):
    if is_square(n):
        return math.isqrt(n)
    c = cf(n)
    c += c[1:]*(100 // len(c))
    f = Fraction(c[-1],1)
    for i in range(len(c) - 1,-1,-1):
        f = 1 / f
        f += c[i]
    return f

def is_square(n):
    if n >= 0 and math.isqrt(n)**2 == n:
        return True
    return False

def dist_func(n):
    if n >= 0:
        cos1 = math.cos(math.sqrt(n)*math.pi)
        dc = math.ceil(cos1) - cos1
        return min(dc,1 - dc)
    pis = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    pi = Fraction(int(pis),10**(len(pis) - 1))
    cos = Fraction(0,1)
    m = (pi*fraction(-n))**2
    a = m
    f = 1
    for i in range(2,300):
        f *= i
        if i % 2 == 0:
            p = a / f
            if p < 10**-20 and p > 0:
                break
            cos += p
            a *= m
    dec = (cos.numerator % cos.denominator) / cos.denominator
    dc = math.ceil(dec) - dec
    return min(dc,1 - dc)


n = 0
md = 1
for i in range(-1000,1001):
    if not is_square(i):
        df = dist_func(i)
        if df < md:
            md = df
            n = i

print(n)

#answer = -163
#15 minutes