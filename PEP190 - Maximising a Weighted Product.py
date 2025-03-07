from fractions import Fraction
import math

def tri_num(n):
    return n*(n + 1) // 2

def next_frac(frac,p):
    f = Fraction(p,p + tri_num(p - 1))
    return frac*f**p*(1 - f)**tri_num(p - 1)

fracs = [Fraction(4,27)]
for i in range(13):
    fracs.append(next_frac(fracs[-1],i + 3))

s = 0
for m in range(2,16):
    s += math.floor(m**tri_num(m)*fracs[m - 2])
print(s)

#answer = 371048281
