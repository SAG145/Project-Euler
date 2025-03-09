import math
import random
def all_bool_primes_below_n(n):
    primes_bool = [False, False] + [True] * (n - 2)
    for k in range(2, int(math.sqrt(n)) + 1):
        if primes_bool[k]:
            for l in range(2*k,n,k):
                primes_bool[l] = False
    return primes_bool

def prob_prime(n):
    for k in range(10):
        if pow(random.randrange(2,n),n - 1,n) != 1:
            return False
    return True

def con_prime(bool_primes,p,q):
    s = str(p)
    r = str(q)
    t = int(s + r)
    if t < len(bool_primes):
        if bool_primes[t]:
            if bool_primes[int(r + s)]:
                return True
            return False
        return False
    if prob_prime(t):
        if prob_prime(int(r + s)):
            return True
    return False


bool_primes = all_bool_primes_below_n(10**8)
print(perf_counter() - start)
primes = []
for n in range(10**6):
    if bool_primes[n]:
        primes.append(n)

breaking = False
for i in range(4,len(primes)):
    if breaking:
        break
    for j in range(3,i):
        if con_prime(bool_primes,primes[i],primes[j]):
            primes_set = (primes[i],primes[j])
            ps1 = primes_set
            for k in range(2,j):
                con = True
                for pr in primes_set:
                    if not con_prime(bool_primes,pr,primes[k]):
                        con = False
                        break
                if con and not breaking:
                    primes_set = ps1 + (primes[k],)
                    ps2 = primes_set
                    for l in range(1,k):
                        con = True
                        for pr in primes_set:
                            if not con_prime(bool_primes,pr,primes[l]):
                                con = False
                                break
                        if con and not breaking:
                            primes_set = ps2 + (primes[l],)
                            ps3 = primes_set
                            print(primes_set)
                            for m in range(l):
                                con = True
                                for pr in primes_set:
                                    if not con_prime(bool_primes,pr,primes[m]):
                                        con = False
                                        break
                                if con and not breaking:
                                    print(sum(primes_set) + primes[m])
                                    breaking = True
                                    break

#answer = 26033
#This code was written after the problem was solved because the original code was lost.
