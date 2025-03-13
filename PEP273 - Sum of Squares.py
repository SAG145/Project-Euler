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

def all_indexes(indexes,b,ones,max_len):
    if len(b) == max_len:
        indexes.append((ones,b))
    else:
        all_indexes(indexes,b + "0",ones,max_len)
        all_indexes(indexes,b + "1",ones + 1,max_len)

def bin_to_primes(b,primes):
    new = []
    for i in range(len(b)):
        if b[i] == "1":
            new.append(primes[i])
    return new

def bin_to_index(b):
    i = 0
    b = b[::-1]
    for j in range(len(b)):
        if b[j] == "1":
            i += 2**j
    return i

def sum_squares(p):
    for t in range(1,math.isqrt(p)):
        s = p - t**2
        if math.isqrt(s)**2 == s and t**2 < s:
            return [(math.isqrt(s),t)]

def nss(ss1,ss2):
    a,b,c,d = ss1[0],ss1[1],ss2[0],ss2[1]
    return [(a*c + b*d,abs(a*d - b*c)),(abs(a*c - b*d),a*d + b*c)]

def new_sum_squares(all_sum_squares,b):
    i1 = b.index("1")
    new = []
    for ss1 in all_sum_squares[bin_to_index(b[:i1] + "0" + b[i1 + 1:])]:
        for ss2 in all_sum_squares[bin_to_index(b[:i1] + "1" + "0"*(len(b) - i1 - 1))]:
            new += nss(ss1,ss2)
    return new

primes = []
for p in all_primes_below_n(150):
    if p % 4 == 1:
        primes.append(p)

indexes = []
all_indexes(indexes,"",0,16)
indexes.sort()

all_sum_squares = [0]*2**16
for i in indexes:
    if i[0] == 1:
        all_sum_squares[bin_to_index(i[1])] = sum_squares(bin_to_primes(i[1],primes)[0])
    elif i[0] != 0:
        all_sum_squares[bin_to_index(i[1])] = new_sum_squares(all_sum_squares,i[1])

sigmaSN = 0
for n in all_sum_squares:
    if n != 0:
        for ss in n:
            sigmaSN += min(ss)

print(sigmaSN)

#Answer = 2032447591196869022
