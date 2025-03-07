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

def num_of_primes_below_n(primes,n):
    a = int(n / math.log(n))
    while primes[a] < n + 1:
        a += 1
    return a

def semi_primes_below(n):
    primes = all_primes_below_n(n // 2)
    print(perf_counter() - start)
    x = len(primes)
    b = 0
    primes.pop(0)
    for p in primes:
        if p > math.sqrt(n):
            break
        a = num_of_primes_below_n(primes,n // p)
        x += a
        b += 1
    return x - b*(b - 1) // 2

print(semi_primes_below(10**8))

#answer = 17427258
