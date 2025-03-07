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
    
def modular_inverse(mod,b):
    n1 = n2 = 0
    n1_lst = [1,0]
    n2_lst = [0,1]
    x = mod
    while mod % b != 0:
        n1 = n1_lst[-2] - (mod // b)*n1_lst[-1]
        n2 = n2_lst[-2] - (mod // b)*n2_lst[-1]
        n1_lst.append(n1)
        n2_lst.append(n2)
        r = mod % b
        mod = b
        b = r
    if n2 > 0:
        return n2
    return n2 + x
    
def least_such_number(a,b):
    mod = 10**len(str(a))
    n = (a*modular_inverse(mod,b))
    return n*b % (b*mod)

primes = all_primes_below_n(10**6 + 10)
sum = 0
for i in range(2,len(primes) - 1):
    n = least_such_number(primes[i],primes[i + 1])
    sum += least_such_number(primes[i],primes[i + 1])
print(sum)

#answer = 18613426663617118
