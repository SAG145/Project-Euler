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
    return (primes_list,primes_bool)

def first_index_larger(lst,elem,index = 0):
    l = len(lst) // 2
    if len(lst) == 0 or lst[-1][0] <= elem:
        return -1
    if lst[l][0] > elem and (lst[l - 1][0] <= elem or len(lst) == 1):
        return index + l
    if lst[l][0] <= elem:
        return first_index_larger(lst[l + 1:],elem,index + l + 1)
    else:
        return first_index_larger(lst[:l], elem, index)

def new_summation(n):
    summ = []
    for p in primes:
        i = first_index_larger(summations[n - p],p - 0.5)
        if p > n//2:
            break
        if i != -1:
            for k in range(i,len(summations[n - p])):
                summ.append([p] + summations[n - p][k])
    if primes_bool[n]:
        summ.append([n])
    return summ

summations = [[[0]],[[0]],[[2]],[[3]]]
apbn = all_primes_below_n(10**5)
primes = apbn[0]
primes_bool = apbn[1]
t = 4
while True:
    summations.append(new_summation(t))
    if len(summations[-1]) > 5000:
        print(t)
        break
    t += 1

#Answer = 71

