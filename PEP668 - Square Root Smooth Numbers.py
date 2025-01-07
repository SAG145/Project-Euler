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

def first_index_larger(lst,elem,index = 0):
    l = len(lst) // 2
    if lst[l] > elem and (len(lst) == 1 or lst[l - 1] <= elem):
        return index + l
    if lst[l] <= elem:
        return first_index_larger(lst[l + 1:],elem,index + l + 1)
    else:
        return first_index_larger(lst[:l], elem, index)

def merge_sorted_lists(lst1,lst2):
    new = []
    i = 0
    j = 0
    while i != len(lst1) or j != len(lst2):
        if i == len(lst1):
            new += lst2[j:]
            j = len(lst2)
        elif j == len(lst2):
            new += lst1[i:]
            i = len(lst1)
        elif lst1[i] < lst2[j]:
            new.append(lst1[i])
            i += 1
        else:
            new.append(lst2[j])
            j += 1
    return new

limit = 10**10
primes = all_primes_below_n(math.isqrt(limit)) + [limit]
numbers = []
for a in range(math.floor(math.log(limit,2)) + 1):
    numbers.append(2**a)

srs = len(numbers) - 2
for i in range(1,len(primes) - 1):
    new = []
    for power in range(math.floor(math.log(limit,primes[i])) + 1):
        new1 = []
        ppow = primes[i]**power
        j = 0
        while j < len(numbers) and numbers[j] <= limit // ppow:
            n = numbers[j]*ppow
            if n > limit:
                break
            if n <= limit and primes[i] < math.sqrt(n) and ppow != 1:
                srs += 1
            if n <= limit // primes[i + 1]:
                new1.append(n)
            j += 1
        new = merge_sorted_lists(new,new1)
    numbers = copy.copy(new)

print(srs)

#answer = 2811077773
#1 hour and 45 minutes