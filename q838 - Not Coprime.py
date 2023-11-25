import math
def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for k in range(3,int(math.sqrt(n))+1,2):
        if n % k == 0:
            return False
    return True

def prime_factors_without_repetitions(n,primes_list):
    if n % 2 == 0:
        if 2 not in primes_list:
            primes_list.append(2)
        return prime_factors_without_repetitions(n // 2, primes_list)
    elif is_prime(n):
        if n not in primes_list:
            primes_list.append(n)
        if 1 in primes_list:
            primes_list.remove(1)
        return primes_list
    else:
        for k in range(3, int(math.sqrt(n)) + 1, 2):
            if n % k == 0:
                if is_prime(k):
                    if k not in primes_list:
                        primes_list.append(k)
                    return prime_factors_without_repetitions(n // k, primes_list)

def share(lst1,lst2):
    for k in lst1:
        if k in lst2:
            return True
    return False

def value(not_co_primes,prime):
    a = 0
    for factors in not_co_primes:
        if prime in factors:
            a += 1
    return a

def update(not_co_primes,primes_3):
    i = 0
    while i < len(not_co_primes):
        if share(not_co_primes[i], primes_3):
            not_co_primes.pop(i)
        else:
            i += 1

primes_3 = []
not_co_primes = []
for p in range(3,10**6,10):
    factors = prime_factors_without_repetitions(p,[])
    if not share(factors,primes_3):
        if len(factors) == 1:
            primes_3.append(factors[0])
        else:
            not_co_primes.append(factors)
update(not_co_primes,primes_3)
while len(not_co_primes) != 0:
        if value(not_co_primes,not_co_primes[0][1]) > value(not_co_primes,not_co_primes[0][0]):
            primes_3.append(not_co_primes[0][1])
            update(not_co_primes,primes_3)
        else:
            primes_3.append(not_co_primes[0][0])
            update(not_co_primes, primes_3)
mult = 1
for k in primes_3:
    mult *= k
sum = math.log(mult)
print(round(sum*10**6) / 10**6)

#answer = 250591.442792