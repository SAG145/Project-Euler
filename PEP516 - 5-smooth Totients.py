import math
def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for k in range(3,int(math.sqrt(n))+1,2):
        if n % k == 0:
            return False
    return True

def disjoint(lst1,lst2):
    return len(list(dict.fromkeys(lst1 + lst2))) == len(lst1) + len(lst2)

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

def hamming1(limit,primes):
    list = []
    if limit == 1:
        return list
    if len(primes) == 1:
        for k in range(min(math.floor(log(primes[0],limit)),1) + 1):
            if k > 0:
                list.append((primes[0]**k,[primes[0]]))
            else:
                list.append((primes[0]**k,[]))
        return list

    for k in range(min(math.floor(log(primes[0],limit)),1) + 1):
        lst = hamming1(limit / primes[0]**k,primes[1:])
        for n in lst:
            if k > 0:
                list.append((n[0]*primes[0]**k,n[1] + [primes[0]]))
            else:
                list.append((n[0]*primes[0]**k,n[1]))
    return list

h = hamming(10**12 + 1,all_primes_below_n(6))
primes = []
for ham in h:
    if is_prime(ham + 1):
        primes.append(ham + 1)
primes.sort()
primes = primes[3:]
print(len(primes))
print(primes)
hprimes = sorted(hamming1(10**6 + 1,primes))
hamming_primes = []
for p in primes:
    if p > 10**6 and p < 10**12:
        hprimes.append((p,[p]))
for i in range(len(hprimes)):
    n = hprimes[i]
    for j in range(i + 1):
        m = hprimes[j]
        if disjoint(n[1],m[1]):
            if n[0]*m[0] < 10**12 + 1:
                for k in range(j + 1):
                    l = hprimes[k]
                    if disjoint(n[1], l[1]) and disjoint(m[1], l[1]):
                        if n[0] * m[0] * l[0] < 10 ** 12 + 1:
                            hamming_primes.append(n[0] * m[0] * l[0])
                        else:
                            break
            else:
                break
hamming_primes = list(dict.fromkeys(hamming_primes))
hamming_primes.sort()
print(len(hamming_primes))
s = 0
target = 10**12
mod = 2**32
a = 0
for n in h:
    print(a,len(h))
    if n % mod != 0:
        i = 0
        limit = target / n
        while i < len(hamming_primes) and hamming_primes[i] <= limit:
            s += n*hamming_primes[i]
            i += 1
    a += 1

print(s % mod)

#answer = 939087315