import math
def prime_factors_with_repetitions(n,primes_list = [],m = 2):
    if n % 2 == 0:
        return prime_factors_with_repetitions(n // 2,primes_list + [2])
    else:
        if m == 2:
            m = 3
        for k in range(m,int(math.sqrt(n)) + 1,2):
            if n % k == 0:
                return prime_factors_with_repetitions(n // k,primes_list + [k],m)
        return primes_list + [n]
