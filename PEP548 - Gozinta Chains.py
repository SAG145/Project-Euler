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

def prime_factors_with_repetitions(n,primes_list = [],m = 2):
    if n == 1:
        return primes_list
    if n % 2 == 0:
        return prime_factors_with_repetitions(n // 2,primes_list + [2])
    else:
        if m == 2:
            m = 3
        for k in range(m,int(math.sqrt(n)) + 1,2):
            if n % k == 0:
                return prime_factors_with_repetitions(n // k,primes_list + [k],m)
        return primes_list + [n]

def min_number_of_form(form,primes_powers):
    n = 1
    for k in range(len(form)):
        n *= primes_powers[k][form[k]]
    return n

def smart_search_index(lst,elem,index = 0):
    if len(lst) == 0:
        return -1
    l = len(lst) // 2
    if lst[l][0] == elem:
        return index + l
    if lst[l][0] < elem:
        return smart_search_index(lst[l + 1:],elem,index + l + 1)
    else:
        return smart_search_index(lst[:l], elem, index)

def smaller(gozintas,power,options,current,i,last):
    if current != power and last != 0:
        options[0] += sorted_powers[len(current)][smart_search_index(sorted_powers[len(current)],tuple(sorted(current)[::-1]))][1]
    if i < len(power[0]):
        smaller(gozintas,power,options,current,i + 1,0)
        for k in range(1,power[0][i] + 1):
            smaller(gozintas,power,options,current + [k],i + 1,k)

def gozinta(gozintas,power):
    v = [1]
    smaller(gozintas,power,v,[],0,0)
    return v[0]

def appears(lst,num):
    a = 0
    for k in lst:
        if k == num:
            a += 1
    return a

def pattern(n):
    pat = []
    pf = prime_factors_with_repetitions(n)
    for k in list(dict.fromkeys(pf)):
        pat.append(appears(pf,k))
    return sorted(pat)[::-1]

def ilog(base,n):
    pow = 0
    a = 1
    while a <= n:
        a *= base
        pow += 1
    return pow - 1

def all_powers(powers,prime_powers,limit,current):
    powers.append(current)
    for k in range(1,ilog(prime_powers[len(current)][1],limit / min_number_of_form(current,prime_powers)) + 1):
        all_powers(powers,prime_powers,limit,current + [k])

primes = all_primes_below_n(100)
primes_powers = []
for p in range(16):
    pow = [1]
    for _ in range(55):
        pow.append(pow[-1]*primes[p])
    primes_powers.append(pow)
powers = []
all_powers(powers,primes_powers,10**16,[])
powers.pop(0)
gozintas = [1]

a = 0
for i in range(len(powers)):
    powers[i].sort()
    powers[i] = tuple(powers[i][::-1])

powers = list(dict.fromkeys(powers))
gozintas = []
sorted_powers = []
for k in range(16):
    gozintas.append([0]*60)
    sorted_powers.append([])

for p in powers:
    sorted_powers[len(p)].append((p,0))

for pow in range(len(sorted_powers)):
    sorted_powers[pow] = sorted(sorted_powers[pow])

s = 1
for i in range(len(sorted_powers)):
    pow = sorted_powers[i]
    l = len(pow)
    for j in range(len(pow)):
        p = pow[j]
        g = gozinta(gozintas,p)
        sorted_powers[i][j] = (sorted_powers[i][j][0],g)
        if g < 10**16:
            if list(p[0]) == pattern(g):
                s += g

print(s)

#Answer = 12144044603581281
