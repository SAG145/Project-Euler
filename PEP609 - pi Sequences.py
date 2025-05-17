import math

def first_index_larger(lst,elem,index = 0):
    l = len(lst) // 2
    if len(lst) == 0:
        return -1
    if lst[l] > elem and (len(lst) == 1 or lst[l - 1] <= elem):
        return index + l
    if lst[l] <= elem:
        return first_index_larger(lst[l + 1:],elem,index + l + 1)
    else:
        return first_index_larger(lst[:l], elem, index)

def all_primes_below_n(n):
    primes_bool = [True]*n
    primes_bool[0] = False
    primes_bool[1] = False
    for k in range(2, math.isqrt(n) + 1):
        if primes_bool[k]:
            for l in range(k**2,n,k):
                primes_bool[l] = False
    primes_list = []
    for k in range(2,n):
        if primes_bool[k]:
            primes_list.append(k)
    return primes_list

def bool_all_primes_below_n(n):
    primes_bool = [True]*n
    primes_bool[0] = False
    primes_bool[1] = False
    for k in range(2, math.isqrt(n) + 1):
        if primes_bool[k]:
            for l in range(k**2,n,k):
                primes_bool[l] = False
    return primes_bool

def pi(primes,n):
    i = first_index_larger(primes,n)
    if i == -1:
        return len(primes)
    return i

def P(n):
    mod = 10**9 + 7
    primes = all_primes_below_n(n)
    boolp = bool_all_primes_below_n(len(primes) + 1)
    pi2 = pi(primes,len(primes))
    t = n
    ml = 1
    while t > 0:
        t = pi(primes,t)
        ml += 1
    p_list = [0]*ml
    p_list[1] = 1
    c_list = [(0,)*ml,(0,1) + (0,)*(ml - 2)]
    pi1 = 0
    for i in range(2,len(primes) + 1):
        if boolp[i]:
            pi1 += 1
        new = [0]*ml
        t1 = 0
        if not boolp[i]:
            t1 += 1
        new[t1] += 1
        t2 = t1
        if not boolp[pi1]:
            t2 += 1
        for j in range(len(c_list[pi1])):
            if c_list[pi1][j] != 0:
                if boolp[i]:
                    new[j] += c_list[pi1][j]
                else:
                    new[j + 1] += c_list[pi1][j]
        if i <= pi2:
            c_list.append(tuple(new))
        if i == len(primes):
            multi = n - primes[i - 1] + 1
        else:
            multi = primes[i] - primes[i - 1]
        for l in range(len(new)):
            if new[l] != 0:
                p_list[l] += new[l]
                p_list[l + 1] += new[l]*(multi - 1)
    m = 1
    for t in p_list:
        if t != 0:
            m *= t
    return m % mod

print(P(10**8))

#Answer = 172023848