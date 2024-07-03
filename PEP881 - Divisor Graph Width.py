import math
import copy
def log(x,y):
    return math.log(y,int(x))

def hamming(limit,primes):
    list = []
    if limit == 1:
        return list
    if len(primes) == 1:
        for k in range(math.floor(log(primes[0],limit)) + 1):
            list.append((primes[0]**k,(primes[0],)*k))
        return list

    for k in range(math.floor(log(primes[0],limit)) + 1):
        lst = hamming(limit / primes[0]**k,primes[1:])
        for n in lst:
            list.append((n[0]*primes[0]**k,n[1] + (primes[0],)*k))
    return list

def first_index_larger(lst,elem,index = 0):
    l = len(lst) // 2
    if lst[l] > elem and (lst[l - 1] <= elem or len(lst) == 1):
        return index + l
    if lst[l] <= elem:
        return first_index_larger(lst[l + 1:],elem,index + l + 1)
    else:
        return first_index_larger(lst[:l], elem, index)

def last_index_smaller(lst,elem,index = 0):
    l = len(lst) // 2
    if len(lst) == 2:
        if lst[0] < elem and lst[1] >= elem:
            return index
        if lst[1] < elem:
            return index + 1
    if lst[l] < elem and (len(lst) == 1 or lst[l + 1] >= elem):
        return index + l
    if lst[l] >= elem:
        return last_index_smaller(lst[:l + 1],elem,index)
    else:
        return last_index_smaller(lst[l:], elem, index + l)

def sub_sums(sums,lst,s,i):
    if i == len(lst):
        sums.append(s)
    else:
        for k in range(lst[i] + 1):
            sub_sums(sums,lst,s + k,i + 1)

def g(pf):
    sums = []
    sub_sums(sums,pf,0,0)
    sums.sort()
    m = 0
    for s in list(dict.fromkeys(sums)):
        if sums[0] == s:
            new = first_index_larger(sums,s)
        elif sums[-1] == s:
            new =  len(sums) - last_index_smaller(sums,s) - 1
        else:
            new = first_index_larger(sums,s) - last_index_smaller(sums,s) - 1

        if new > m:
            m = new
    return m

target = 10**4
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,73,79,83,89,97]
pf = [1]
while g(pf) < target:
    pf.append(1)

for num in sorted(hamming(primes[len(pf) - 1]*primes[len(pf) - 2]*primes[len(pf) - 3]*primes[len(pf) - 4],primes[:len(pf) - 4]))[1:]:
    npf = copy.copy(pf)
    npf = npf[:-4]
    for p in num[1]:
        npf[primes.index(p)] += 1
    if g(npf) >= target:
        pf = copy.copy(npf)
        break

num = 1
for i in range(len(pf)):
    num *= primes[i]**pf[i]
print(num)

#answer = 205702861096933200