import math
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

def log(a,b):
    return math.floor(math.log(b,a)) + 1

def M(p,q,N):
    max = 0
    for lp in range(1,log(p,N / q)):
        for lq in range(1,log(q,N / p)):
            res = p**lp*q**lq
            if res < N + 1:
                if res > max:
                    max = res
    return max

def S(N):
    primes = all_primes_below_n(N // 2)
    good_p = all_primes_below_n(math.floor(math.sqrt(N)))
    sum = 0
    for p in range(len(good_p)):
        for q in range(p + 1,len(primes)):
            m = M(primes[p],primes[q],N)
            sum += m
            if m == 0:
                break
    return sum

print(S(10**7))

#answer = 11109800204052