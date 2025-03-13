import math

def all_min_pf_below_n(n):
    min_pf = []
    for _ in range(n):
        min_pf.append((0,))
    for k in range(2,int(math.sqrt(n)) + 1):
        if min_pf[k][0] == 0:
            for l in range(2*k,n,k):
                if min_pf[l][0] == 0:
                    min_pf[l] = (k,)
    return min_pf

def all_prime_factorisations_below_n(n):
    min_pf = all_min_pf_below_n(n)
    pf = [0,[]]
    for k in range(2,n):
        mpf = min_pf[k][0]
        if mpf == 0:
            pf.append((k,))
        else:
            pf.append(pf[k // mpf] + (mpf,))
    return pf

def appears(lst,k):
    a = 0
    for n in lst:
        if n == k:
            a += 1
    return a

def shortened_pf(pf):
    spf = []
    for p in list(dict.fromkeys(pf)):
        spf.append((p,appears(pf,p)))
    return spf

def M(n,spf):
    m = 0
    for p in spf:
        v = p[0]**p[1]
        if v > m:
            m = v
    for mm in range(n - m,0,-m):
        if (mm + 1)**2 % n == mm + 1:
            return mm + 1
        if mm**2 % n == mm:
            return mm
    return 1

pf = all_prime_factorisations_below_n(10**7 + 1)
s = 0
for n in range(2,10**7 + 1):
    m = M(n,shortened_pf(pf[n]))
    s += m

print(s)

#Answer = 39782849136421

#Time: 15:00
