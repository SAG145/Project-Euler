import math

def is_prime(n):
    if n % 2 == 0:
        return False
    for k in range(3,int(math.sqrt(n))+1,2):
        if n % k == 0:
            return False
    return True
def prime_factors_without_repetitions(n,primes_list = []):
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


def is_permutation(n1,n2):
    lst1,lst2 = [],[]
    for k in str(n1):
        lst1.append(int(k))
    for j in str(n2):
        lst2.append(int(j))
    return sorted(lst1) == sorted(lst2)

def euler_function(n):
    mult = n
    list = prime_factors_without_repetitions(n,[])
    for num in list:
        mult *= (1-1/num)
    return int(mult)

x = 10000
min = 0
for i in range(3,10**7):
    e = euler_function(i)
    if i/e < x:
        if is_permutation(i,e):
            x = i/e
            min = i
print(min)
#answer = 8319823