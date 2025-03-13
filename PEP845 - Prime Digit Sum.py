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

def partition(n,partitions):
    new = []
    if n < 10:
        new.append((n,))
    for k in range(max(1,n - 9),n):
        for p in partitions[k]:
            if len(p) < 18:
                new.append(tuple(sorted(p + (n - k,))))
    partitions.append(list(dict.fromkeys(new)))

partitions = [[(0,)],[(1,)],[(1,1),(2,)]]
for n in range(3,163):
    partition(n,partitions)

factorial = []
for k in range(20):
    factorial.append(math.factorial(k))

def permutation(part,zero):
    lst = [zero] + [0]*9
    for i in part:
        lst[i] += 1
    m = factorial[sum(lst)]
    for k in lst:
        m = m // factorial[k]
    return m

for i in range(len(partitions)):
    p = partitions[i]
    new = []
    for l in range(19):
        new.append([])
    for part in p:
        new[len(part)].append(part)
    for len1 in new:
        len1.sort()
    partitions[i] = copy.deepcopy(new)

def next_digit(partitions,target,max_len,s):
    pds = 0
    digit = 0
    while pds <= target:
        ppds = pds
        for prime in all_primes_below_n(162):
            if prime - digit - s >= 0:
                p = partitions[prime - digit - s]
                for q in p[:max_len + 1]:
                    for r in q:
                        pds += permutation(r, max_len - len(r))
        digit += 1
    return (digit - 1,target - ppds)

target = 10**16
ml = 18
x = 0
s = 0
while target != 1:
    nd = next_digit(partitions,target,ml,s)
    x += nd[0]*10**ml
    s += nd[0]
    target = nd[1]
    ml -= 1

print(x)

#Answer = 45009328011709400
