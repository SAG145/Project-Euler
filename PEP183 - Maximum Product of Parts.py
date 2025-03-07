import math

def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for k in range(3,int(math.sqrt(n))+1,2):
        if n % k == 0:
            return False
    return True

def prime_factors_with_repetitions(n,primes_list):
    if n % 2 == 0:
        primes_list.append(2)
        return prime_factors_with_repetitions(n/2,primes_list)
    elif is_prime(n):
        primes_list.append(int(n))
        return primes_list
    else:
        for k in range(3,int(math.sqrt(n))+1,2):
            if n % k == 0:
                if is_prime(k):
                    primes_list.append(k)
                    return prime_factors_with_repetitions(n/k,primes_list)

def D(n):
    n_max = round(n / math.e)                                     #לזה הגעתי על ידי פתרון בעיית קיצון של הפונקציה
    n_primes = prime_factors_with_repetitions(n,[])               # f(x) = (a/x)**x
    max_primes = prime_factors_with_repetitions(n_max,[])
    for p1 in n_primes:
        if p1 in max_primes:
            max_primes.remove(p1)

    for p2 in max_primes:
        if p2 != 1 and p2 != 2 and p2 != 5:
            return n
    return -n

x = 0
for k in range(5,10001):
    x += D(k)
print(x)

#answer = 48861552
