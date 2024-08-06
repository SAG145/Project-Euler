import math
def prime_factors_with_repetitions(n,primes_list):
    if n % 2 == 0:
        primes_list.append(2)
        return prime_factors_with_repetitions(n // 2,primes_list)
    else:
        for k in range(3,int(math.sqrt(n)) + 1,2):
            if n % k == 0:
                primes_list.append(k)
                return prime_factors_with_repetitions(n // k,primes_list)
    return primes_list + [n]

def divi(n):
    if n == 2:
        return 2
    d = divi(n - 1)
    pf = prime_factors_with_repetitions(d, [])
    for p in prime_factors_with_repetitions(n, []):
        if p in pf:
            pf.remove(p)
        else:
            d *= p
    return d


def p(s, n):
    if s == 1:
        return (n - 1) // 2
    return (n - 1) // divi(s) - (n - 1) // divi(s + 1)


x = 0
for i in range(1,32):
    x += p(i, 4**i)
print(x)

# answer = 1617243
