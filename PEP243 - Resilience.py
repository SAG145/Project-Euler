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

def euler_function(n):
    mult = n
    list = prime_factors_without_repetitions(n,[])
    for num in list:
        mult *= (1-1/num)
    return int(mult)

def r_func(n):
    return euler_function(n)/(n-1)

print(2*2*2*3*5*7*11*13*17*19*23)

#Answer = 892371480

#a = 15499/94744
# r_func(2*3*5*7*11*13*17*19*23) is greater than a.
# r_func(2*3*5*7*11*13*17*19*23*29) is smaller than a.
#For any n that is a product of consecutive primes (starting from 2) each of which appears exactly once in its factorisation,
#The value of r_func(n) is the minimum between all numbers up to n.
#Therefore the solution to the question will be between these two numbers, and after some trial and error we arrive at the solution.
