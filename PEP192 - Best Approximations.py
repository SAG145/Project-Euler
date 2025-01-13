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

def cf_to_fraction(cf1):
    f = Fraction(cf1[-1],1)
    for i in range(len(cf1) - 2,-1,-1):
        f = 1 / f
        f += cf1[i]
    return f

def all_fractions(n,bound):
    fras = []
    cf1 = cf(n)
    cf1 += cf1[1:]*(100 // len(cf1))
    for i in range(1,len(cf1)):
        f = cf_to_fraction(cf1[:i])
        if f.denominator < bound:
            fras.append(f)
        else:
            break
    return fras

def first_m_larger(n1,n2,d1,d2,sqrt1,r1 = 0 ,r2 = 1000):
    if r1 > 1000:
        return 2000
    m = (r1 + r2) // 2
    f = Fraction(n1 + m*n2,d1 + m*d2)
    if f > sqrt1 and (r1 == m or Fraction(n1 + (m - 1)*n2,d1 + (m - 1)*d2) < sqrt1):
        return m
    if f < sqrt1:
        return first_m_larger(n1,n2,d1,d2,sqrt1,m + 1,r2)
    else:
        return first_m_larger(n1,n2,d1,d2,sqrt1,r1,m)

def last_m_larger(n1,n2,d1,d2,sqrt1,r1 = 0,r2 = 1000):
    m = (r1 + r2) // 2
    f = Fraction(n1 + m*n2,d1 + m*d2)
    if f > sqrt1 and (r1 == m or Fraction(n1 + (m + 1)*n2,d1 + (m + 1)*d2) < sqrt1):
        return m
    if f > sqrt1:
        return last_m_larger(n1,n2,d1,d2,sqrt1,m + 1,r2)
    else:
        return last_m_larger(n1,n2,d1,d2,sqrt1,r1,m)

def best_appro(n,bound):
    bi = -1
    af = []
    cf1 = cf(n)
    cf1 += cf1[1:] * (100 // len(cf1))
    for i in range(1,len(cf1)):
        f = cf_to_fraction(cf1[:i])
        if f.denominator < bound:
            af.append(f)
            if f.denominator > bound and bi == -1:
                bi = i - 2
        else:
            break

    p = af[1].numerator
    q = af[1].denominator
    sqrt1 = cf_to_fraction(cf1 + cf1[1:])
    den = q
    md = abs(Fraction(p,q) - sqrt1)
    for j in range(bi,len(af) - 1):
        n1,n2 = af[j].numerator,af[j + 1].numerator
        d1,d2 = af[j].denominator,af[j + 1].denominator
        if Fraction(n1,d1) < sqrt1:
            m = first_m_larger(n1,n2,d1,d2,sqrt1)
        else:
            m = last_m_larger(n1,n2,d1,d2,sqrt1)
        o = (bound - d1) // d2
        f1 = Fraction(n1 + m*n2,d1 + m*d2)
        f2 = Fraction(n1 + (m - 1)*n2,d1 + (m - 1)*d2)
        f3 = Fraction(n1 + o*n2,d1 + o*d2)
        if f1.denominator < bound and abs(f1 - sqrt1) < md:
            md = abs(f1 - sqrt1)
            den = f1.denominator
        if f2.denominator < bound and abs(f2 - sqrt1) < md:
            md = abs(f2 - sqrt1)
            den = f2.denominator
        if f3.denominator < bound and abs(f3 - sqrt1) < md:
            md = abs(f3 - sqrt1)
            den = f3.denominator
    return den

s = 0
for n in range(10**5 + 1):
    if math.isqrt(n)**2 != n:
        s += best_appro(n,10**12)
print(s)

#answer = 57060635927998347
#6 minutes