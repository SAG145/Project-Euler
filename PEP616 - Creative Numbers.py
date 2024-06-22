import math
def all_primes_below_n_bool(n):
    primes_bool = [False, False] + [True] * (n - 2)
    for k in range(2, int(math.sqrt(n)) + 1):
        if primes_bool[k]:
            for l in range(2*k,n,k):
                primes_bool[l] = False
    return primes_bool

primes = all_primes_below_n_bool(10**6 + 1)
creative = []
for a in range(2,10**6 + 1):
    b = 2
    while a**b <= 10**12:
        if not primes[a] or not primes[b]:
            creative.append(a**b)
        b += 1

creative = list(dict.fromkeys(creative))

print(sum(creative) - 16)