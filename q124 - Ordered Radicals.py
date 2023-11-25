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
        return prime_factors_without_repetitions(n / 2, primes_list)
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
                    return prime_factors_without_repetitions(n / k, primes_list)

def multiple_list(lst):
    mult = 1
    for k in lst:
        mult *= k
    return int(mult)

def rad(n):
    return multiple_list(prime_factors_without_repetitions(n,[]))

def E(k):
    rad_list = []
    for n in range(1,100001):
        rad_list.append((rad(n),n))
    rad_list.sort()
    return rad_list[k-1][1]
print(E(10000))

#answer = 21417