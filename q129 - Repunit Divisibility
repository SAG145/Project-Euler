import math
def prime_factors_with_repetitions(n,primes_list,m = 2):
    if n % 2 == 0:
        primes_list.append(2)
        return prime_factors_with_repetitions(n // 2, primes_list)
    if n == 1:
        return primes_list
    else:
        if m == 2:
            m = 3
        for k in range(m, int(math.sqrt(n)) + 1, 2):
            if n % k == 0:
                primes_list.append(k)
                return prime_factors_with_repetitions(n // k, primes_list,k)
    primes_list.append(n)
    return primes_list
    
def R(k):
    return int("1"*k)

def divisors(n):
    divi = []
    for k in range(2,math.floor(math.sqrt(n) + 1)):
        if n % k == 0:
                divi.append(k)
                divi.append(n // k)
    return sorted(divi)
    
def gcd(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
    
def lcm(a,b):
    return a*b // gcd(a,b)
    
def euler_function(n,primes):
    for p in primes:
        n *= (1 - 1 / p)
    return round(n)
    
def max_power(n,p):
    a = p
    while n % a == 0:
        a *= p
    return a // p
    
def A(n):
    pf = prime_factors_with_repetitions(n,[])
    pf = list(dict.fromkeys(pf))
    if 3 in pf:
        p = max_power(n,3)
        return lcm(p,A(n // p))
    mini = euler_function(n,pf)
    options = divisors(mini)
    for d in options:
        if R(d) % n == 0:
            return d
    return mini
    
n = 10**6 + 1
while True:
    if n % 5 != 0:
        a = A(n)
        if a > 10**6:
            print(n)
            break
    n += 2
    
#answer = 1000023
