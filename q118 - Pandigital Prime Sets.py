import copy
import itertools
import math
def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for k in range(3,int(math.sqrt(n))+1,2):
        if n % k == 0:
            return False
    return True

def num_of_times(lst,elem):
    n = 0
    for k in lst:
        if k == elem:
            n += 1
    return n

def factorial_list(lst):
    lst1 = list(dict.fromkeys(lst))
    m = 1
    for k in lst1:
        m *= math.factorial(num_of_times(lst,k))
    return m

def partitions(n):
    if n == 1:
        return [[1]]
    p = partitions(n - 1)
    part = []
    for par in p:
        for k in range(len(par)):
            par1 = copy.copy(par)
            par1[k] += 1
            part.append(sorted(par1))
        part.append([1] + par)
    return remove_dup(sorted(part))

def remove_dup(list):
    i = 0
    while i < len(list) - 1:
        if list[i] == list[i + 1]:
            list.pop(i)
        else:
            i += 1
    return list

def repeating_digit(num):
    return not len(num) == len(set(num))

def tuple_to_str(t):
    s = ""
    for c in t:
        s += c
    return s

def substrings(str1):
    if len(str1) == 1:
        return [str1,""]
    subg = []
    subs = substrings(str1[1:])
    subg += subs
    a = str1[0]
    for g in subs:
        subg.append(a + g)
    return subg

def num_of_sets(partition,set1,primes,sets):
    if len(set1) == 9:
        sets[0] += 1
    else:
        for p in primes[partition[0]]:
            set2 = set1 + p
            if not repeating_digit(set2):
                num_of_sets(partition[1:],set2,primes,sets)

partitions_of_9 = []
for p in partitions(9):
    if num_of_times(p,1) < 5 and 9 not in p:
        partitions_of_9.append(p)

primes = []
for i in range(9):
    primes.append([])
a = 0
for sub in substrings("123456789"):
    a += 1
    if sub != "" and sub != "1":
        l = len(sub)
        for p in itertools.permutations(sub):
            s = tuple_to_str(p)
            if is_prime(int(s)):
                primes[l].append(s)

pandigital_sets = 0
for part in partitions_of_9:
    sets = [0]
    num_of_sets(part,"",primes,sets)
    pandigital_sets += sets[0] // factorial_list(part)
print(pandigital_sets)

#answer = 44680