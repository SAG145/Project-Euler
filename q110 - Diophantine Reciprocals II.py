import math
import copy
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

def prime_factors_with_repetitions(n,primes_list,m = 2):
    if n == 1:
        return primes_list
    if n % 2 == 0:
        primes_list.append(2)
        return prime_factors_with_repetitions(n // 2,primes_list)
    else:
        if m == 2:
            m = 3
        for k in range(m,int(math.sqrt(n)) + 1,2):
            if n % k == 0:
                primes_list.append(k)
                return prime_factors_with_repetitions(n // k,primes_list,k)
    return primes_list + [n]

def log(x,y):
    return math.log(y,int(x))

def hamming(limit,primes):
    list = []
    if limit == 1:
        return list
    if len(primes) == 1:
        for k in range(math.floor(log(primes[0],limit)) + 1):
            list.append(primes[0]**k)
        return list

    for k in range(math.floor(log(primes[0],limit)) + 1):
        lst = hamming(limit / primes[0]**k,primes[1:])
        for n in lst:
            list.append(n*primes[0]**k)
    return list

def pf_to_powers(pf,primes):
    powers = [0]*(primes.index(pf[-1]) + 1)
    for p in pf:
        powers[primes.index(p)] += 1
    return powers

def opti_mult_list(lst):
    m = 1
    for k in lst:
        m *= (k + 1)
    return m

def mult_list(lst):
    m = 1
    for k in lst:
        m *= k
    return m

def minus_lists(lst1,lst2):
    lst = copy.copy(lst1)
    for k in lst2:
        lst.remove(k)
    return lst

def subgroups(lst):
    if len(lst) == 1:
        return [lst,[]]
    subg = []
    subs = subgroups(lst[1:])
    subg += subs
    a = [lst[0]]
    for g in subs:
        subg.append(a + g)
    return subg

def plus_elements(lst1,lst2):
    lst = copy.copy(lst1)
    for i in range(len(lst2)):
        lst[i] += lst2[i]
    return lst

def num_solutions(lst):
    s = subgroups(lst)
    solutions = 0
    for l in s:
        t = opti_mult_list(minus_lists(lst,l))
        solutions += mult_list(l)*t
    return (solutions + 1) // 2


def least_n(min_solutions):
    primes = all_primes_below_n(100)
    solution_powers = [1]
    while num_solutions(solution_powers) < min_solutions:
        solution_powers.append(1)
    change = True
    while change:
        change = False
        p = primes[len(solution_powers) - 1]
        s = copy.copy(solution_powers)
        k = p
        for n in hamming(p,all_primes_below_n(p)):
            if n < k and n != 1:
                lst = copy.copy(solution_powers)
                lst.pop(-1)
                a = prime_factors_with_repetitions(n,[])
                b = pf_to_powers(a,primes)
                c = plus_elements(lst,b)
                if num_solutions(c) > min_solutions - 1:
                    s = plus_elements(lst,b)
                    k = n
                    change = True
        solution_powers = s
    solution = 1
    for i in range(len(solution_powers)):
        solution *= primes[i]**solution_powers[i]
    return solution

print(least_n(4000000))

#answer = 9350130049860600