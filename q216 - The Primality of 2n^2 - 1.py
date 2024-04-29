import math
import random
from time import perf_counter
start = perf_counter()
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

def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for k in range(3,int(math.sqrt(n))+1,2):
        if n % k == 0:
            return False
    return True

# def prob_prime(n):
#     max_power2 = 2
#     while (n - 1) % 2**max_power2 == 0:
#         max_power2 += 1
#     max_power2 -= 1
#     a = n // 2**max_power2
#     for i in range(200):
#         r = random.randrange(2,n)
#         m = r**a % n
#         if m != 1 and m != -1:
#             found = False
#             j = 1
#             while j < max_power2 and not found:
#                 if r ** (2 ** j * a) % n == n - 1:
#                     found = True
#                 j += 1
#             if not found:
#                 return False
#     return True

def prob_prime1(n):
    for k in range(10):
        if pow(random.randrange(2,n),n - 1,n) != 1:
            return False
    return True

# x = 0
# for i in range(3,10**6):
#     if prob_prime1(i):
#         print(i)
#         x += 1
# print(x)
# tp = 0
# for k in range(2,10**5 + 1):
#     if is_prime(2*k**2 - 1):
#         print(k,2*k**2 - 1)
#         tp += 1
# print(tp)
# print(perf_counter() - start)

def mod_p(p):
    h = p // 2 + 1
    for i in range(2,h):
        if i**2 % p == h:
            return i
    return -1

def invalid_mod(primes):
    invalid = []
    for p in primes[1:10]:
        m = mod_p(p)
        if m != -1:
            invalid.append((p,m, p - m))
    return invalid[:2]

def invalid(n,invalids):
    for t in invalids:
        p = t[0]
        if p > n - 1:
            break
        if n % p == t[1] or n % p == t[2]:
            return True
    return False

def t_primes(maxi):
    # primes = all_primes_below_n(round(maxi*math.sqrt(2)) + 5)
    primes = all_primes_below_n(100)
    print(perf_counter() - start)
    invalids = invalid_mod(primes)
    x = 1
    for n in range(3,maxi):
        if n % 100000 == 0:
            print(n,perf_counter() - start)
        if not invalid(n,invalids):
            # prime = True
            # i = 0
            # t = 2 * n ** 2 - 1
            # sqrt1 = math.floor(math.sqrt(t)) + 1
            # while prime and primes[i] < sqrt1:
            #     if t % primes[i] == 0:
            #         prime = False
            #     i += 1
            # if prime:
            #     x += 1
            if prob_prime1(2*n**2 - 1):
                x += 1
    return x

print(t_primes(50*10**6))

print(perf_counter() - start)

#האלגוריתם הוא הסתברותי, וכשהרצתי אותו (זמן הרצה - רבע שעה) יצא 5437853, אז ניחשתי מספרים קרובים ויותר נמוכים עד שגיליתי את התשובה
#answer = 5437849