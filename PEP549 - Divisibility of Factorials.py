import math
import sys

sys.setrecursionlimit(10**3 + 500)

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

def min_power_divides(n,p):
    pow = 0
    a = p
    while n % a == 0:
        pow += 1
        a *= p
    return pow

def min_fac_divi(p,pow):
    a = 1
    powers = 0
    while pow > powers:
        powers += 1 + min_power_divides(a,p)
        a += 1
    return (a - 1)*p

def sub_s(s,n,take_in_count,start,min_fac_divi_list,primes,si,num,i):
    if i == len(primes) or num*primes[i] > n:
        s[0] += start
        take_in_count[num] = True
    else:
        sub_s(s,n,take_in_count,start,min_fac_divi_list,primes,si,num,i + 1)
        if i != si:
            j = 1
            while primes[i]**j*num <= n and min_fac_divi_list[primes[i]][j] <= start:
                if not take_in_count[primes[i]**j*num]:
                    sub_s(s,n,take_in_count,start,min_fac_divi_list,primes,si,num*primes[i]**j,i + 1)
                j += 1

n = 10**8
primes = all_primes_below_n(math.isqrt(n))
take_in_count = [False]*(n + 1)
min_fac_divi_list = [-1]
pre = 0
for p in primes:
    min_fac_divi_list += [-1]*(p - pre - 1)
    min_fac_pow = [0]
    for pow in range(1,math.floor(math.log(n,p)) + 1):
        min_fac_pow.append(min_fac_divi(p,pow))
    min_fac_divi_list.append(min_fac_pow)
    pre = p

s = [0]
for big_prime in all_primes_below_n(n):
    if big_prime > math.isqrt(n):
        s[0] += big_prime*(n // big_prime)

for i in range(len(primes)):
    for j in range(1,len(min_fac_divi_list[primes[i]])):
        sub_s(s,n,take_in_count,min_fac_divi_list[primes[i]][j],min_fac_divi_list,primes,i,primes[i]**j,0)

print(s[0])

#Answer = 476001479068717

#Time: 1:30
