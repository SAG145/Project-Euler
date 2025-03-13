import math

def In(n):
    for t in range(2,n):
        if t**2 % n == 1:
            return n - t

def all_min_pf_below_n(n):
    min_pf = [0]*n
    for k in range(2,int(math.sqrt(n)) + 1):
        if min_pf[k] == 0:
            for l in range(2*k,n,k):
                if min_pf[l] == 0:
                    min_pf[l] = k
    return min_pf

def extended_Euclid(n,mod):
    if n < mod:
        return extended_Euclid(mod,n)[::-1]
    while n % mod != 0:
        i = extended_Euclid(mod,n % mod)
        q = n // mod
        return (i[1],i[0] - q*i[1])
    return (0,1)

def inverse(n,mod):
    return extended_Euclid(n,mod)[0] % mod

def solution(a,n,mod):
    return mod // n*inverse(inverse(a,n)*mod // n,n) % mod

def chinese_reminder(a,n,b,m):
    return (solution(a,n,n*m) + solution(b,m,n*m)) % (n*m)

def I(inverses,n):
    m = 0
    for i in inverses:
        if i > m and i != n - 1:
            m = i
    return m

def max_power_divides(n,p):
    a = p
    while n % a == 0:
        a *= p
    return a // p

all_mpf = all_min_pf_below_n(2*10**7 + 1)

inverses = [0,(1,),(1,),(1,2)]
sigma = 1
for k in range(4,2*10**7 + 1):
    mpf = all_mpf[k]
    if mpf == 0:
        mpf = k
    power = max_power_divides(k,mpf)
    if power == k:
        if mpf == 2 and k != 4:
            inverses.append((1,k - 1,k // 2 + 1,k // 2 - 1))
        else:
            inverses.append((1, k - 1))
    else:
        new = []
        for i in inverses[k // power]:
            for j in inverses[power]:
                new.append(chinese_reminder(i,k // power,j,power))
        inverses.append(tuple(new))
    si = sigma
    sigma += I(inverses[-1],k)

print(sigma)

#Answer = 153651073760956

#Time: 27:00
