import math

def mult(lst):
    m = 1
    for a in lst:
        m *= a
    return m

def all_primes_below_n(n):
    primes_bool = [False, False] + [True] * (n - 2)
    for k in range(2, int(math.sqrt(n)) + 1):
        if primes_bool[k]:
            for l in range(2*k,n,k):
                primes_bool[l] = False
    primes_list = []
    for k in range(n):
        if primes_bool[k]:
            primes_list.append(k)
    return primes_list

def all_divisors(divi,pf,curr = 1,i = 0):
    if i < len(pf):
        divi.append(curr*pf[i])
        all_divisors(divi,pf,curr*pf[i],i + 1)
        all_divisors(divi,pf,curr,i + 1)

primes = all_primes_below_n(190)
sta = primes[:len(primes) // 2]
end = primes[len(primes) // 2:]
divs = []
dive = []
all_divisors(divs,sta)
all_divisors(dive,end)
divs.sort()
dive.sort()

target = math.isqrt(mult(primes))
PSR = mult(sta)
a = 0
i = len(dive) - 1

for d in divs:
    a += 1
    while i > 0 and dive[i]*d > target:
        i -= 1
    if dive[i]*d > PSR:
        PSR = dive[i]*d

print(PSR % 10**16)

#Answer = 1096883702440585
