import math

def first_index_larger(lst,elem,index = 0):
    l = len(lst) // 2
    if lst[l] > elem and (len(lst) == 1 or lst[l - 1] <= elem):
        return index + l
    if lst[l] <= elem:
        return first_index_larger(lst[l + 1:],elem,index + l + 1)
    else:
        return first_index_larger(lst[:l], elem, index)

def prime_factors(n,primes_list = [],m = 2):
    if n == 1:
        return primes_list
    if n % 2 == 0:
        return prime_factors(n // 2,primes_list + [2])
    else:
        if m == 2:
            m = 3
        for k in range(m,int(math.sqrt(n)) + 1,2):
            if n % k == 0:
                return prime_factors(n // k,primes_list + [k],m)
        return primes_list + [n]

def shortened_pf(pf):
    spf = []
    i = 1
    p = pf[0]
    pp = 1
    while i < len(pf) + 1:
        if i == len(pf) or pf[i] != p:
            spf.append((p,pp))
            if i != len(pf):
                p = pf[i]
                pp = 1
        else:
            pp += 1
        i += 1
    return spf

def spf(n):
    return shortened_pf(prime_factors(n))

def divisors_from_pf(pf):
    divi = [1]
    for p in pf:
        new = []
        for power in range(p[1] + 1):
            for d in divi:
                new.append(p[0]**power*d)
        divi = new
    return sorted(divi)

def largest_div_smaller(pf,n):
    m1 = 1
    for a in pf:
        m1 *= a[1] + 1
    m2 = 1
    i = 0
    while m2**2 < m1:
        m2 *= pf[i][1] + 1
        i += 1
    divi1 = divisors_from_pf(pf[:i - 1])
    divi2 = divisors_from_pf(pf[i - 1:])
    maxi = 0
    for d in divi1:
        if divi2[-1] >= n / d:
            j = first_index_larger(divi2,n / d) - 1
            if d*divi2[j] > maxi:
                maxi = d*divi2[j]
    return maxi

def div_close_cbrt(n):
    pf = spf(n)
    m1 = 1
    for a in pf:
        m1 *= a[1] + 1
    m2 = 1
    i = 0
    while m2**2 < m1:
        m2 *= pf[i][1] + 1
        i += 1
    divi1 = divisors_from_pf(pf[:i - 1])
    divi2 = divisors_from_pf(pf[i - 1:])
    divi_cbrt = []
    t = math.cbrt(n)
    for d in divi1:
        if d > t:
            break
        j = first_index_larger(divi2,t / d)
        k = j - 1
        while k >= 0 and t / (d*divi2[k]) < 1.0001:
            divi_cbrt.append(d*divi2[k])
            k -= 1
    return sorted(divi_cbrt)

def f(n):
    mini = 10**100
    s = 0
    r = 0
    for a in div_close_cbrt(n):
        r += 1
        b = largest_div_smaller(spf(n // a),math.sqrt(n / a))
        c = n // (a*b)
        if a < b < c and c / a < mini:
            s = a + b + c
            mini = c / a
    return s

print(f(math.factorial(43)))

#Answer = 1177163565297340320