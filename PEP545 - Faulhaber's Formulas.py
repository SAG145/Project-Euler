def primes1(n):
    bp = [True]*(n // 2)
    for i in range(1,n + 1):
        j = 1
        while i + j + 2*i*j < len(bp) and j <= i:
            bp[i + j + 2*i*j] = False
            j += 1
    primes = [2]
    for k in range(1,len(bp)):
        if bp[k]:
            primes.append(2*k + 1)
    return primes

limit = 10**9
sieve = [True]*limit
pf = [2,3,5,23,29]
for p in primes1(limit):
    if sieve[p - 1] and p not in pf:
        for i in range(p - 1,len(sieve),p - 1):
            sieve[i] = False

f = 0
for a in range(308,len(sieve),308):
    if sieve[a]:
        f += 1
        if f == 10**5:
            break

print(a)

#answer = 921107572
#7 hours and 30 minutes