import math
def bool_all_primes_below_n(n):
    primes_bool = [False, False] + [True] * (n - 2)
    for k in range(2, int(math.sqrt(n)) + 1):
        if primes_bool[k]:
            for l in range(2*k,n,k):
                primes_bool[l] = False
    return primes_bool

def first_tile(n):
    if n == 0:
        return 1
    return 2 + 6*(n*(n - 1) // 2)

def num_of_primes(primes,diffs):
    pd = 0
    for k in diffs:
        if primes[k]:
            pd += 1
    return pd

primes = bool_all_primes_below_n(10**6)
n = 1
pd3 = 1
last_pd3_tile = 1
pd3_tiles = []
while pd3 < 2000:
    f = first_tile(n)
    l = f + 6*n - 1
    pft = first_tile(n - 1)
    nft = first_tile(n + 1)
    fpd = [6*n - 1,nft + 1 - f,nft + 6*(n + 1) - 1 - f]
    lpd = [6*n - 1,nft + 6*(n + 1) - 2 - l,l - pft]
    if num_of_primes(primes,fpd) == 3:
        pd3 += 1
        last_pd3_tile = f
    if pd3 < 2000 and num_of_primes(primes,lpd) == 3:
        pd3 += 1
        last_pd3_tile = l
    n += 1

print(last_pd3_tile)

#answer = 14516824220