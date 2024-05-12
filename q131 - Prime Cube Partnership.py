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

def is_cube(n):
    return math.floor(math.cbrt(n))**3 == n

def solution(n,primes):
    solutions = []
    for p in primes:
        if is_cube(n**3 + n**2*p):
            return p
    return 0

primes = all_primes_below_n(10**6 + 10**5)
primes_solutions = []
num_of_prime_solutions = 0
n = 1
while True:
    s = solution(n**3,primes)
    if s > 10**6:
        print(num_of_prime_solutions)
        break
    if s != 0:
        num_of_prime_solutions += 1
    n += 1

#answer = 173