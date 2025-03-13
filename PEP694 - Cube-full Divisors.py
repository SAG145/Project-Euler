import math
import sys

sys.setrecursionlimit(10**5)

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

def all_cube_fulls(cube_fulls,primes,limit,cf,i):
    if i == len(primes) or primes[i]**3*cf > limit:
        cube_fulls.append(cf)
    else:
        all_cube_fulls(cube_fulls,primes,limit,cf,i + 1)
        a = primes[i]**3
        while cf*a <= limit:
            all_cube_fulls(cube_fulls,primes,limit,cf*a,i + 1)
            a *= primes[i]

limit = 10**18
primes = all_primes_below_n(math.ceil(math.cbrt(limit)))
cube_fulls = []
all_cube_fulls(cube_fulls,primes,limit,1,0)
s = 0
for cf in cube_fulls:
    s += limit // cf
print(s)

#Answer = 1339784153569958487
