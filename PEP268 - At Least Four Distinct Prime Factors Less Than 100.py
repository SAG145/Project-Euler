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

def mult_list(lst):
    m = 1
    for k in lst:
        m *= k
    return m

def choose(n,k):
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)

lst = [0,0,0,0,1]
for k in range(5,14):
    a = 0
    for i in range(k):
        a += choose(k,i)*lst[i]
    lst.append(1 - a)

div_by_4 = 0
subs = subgroups(all_primes_below_n(100))
for g in subs:
    if 4 <= len(g) <= 13:
        div_by_4 += lst[len(g)]*(10**16 // mult_list(g))

print(div_by_4)

#Answer = 785478606870985

#Time: 1:30
