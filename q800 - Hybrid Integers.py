import math

log = 800800*math.log(800800)
def less(p,q):
    return p*math.log(q) + q*math.log(p) <= log

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

def solution(p):
    num = 0.1
    for power in range(7,-1,-1):
        for d in range(1,10):
            if not less(p,num + 10**power*d):
                num += 10**power*(d - 1)
                break
            if d == 9:
                num += 10**power*9
    return num
def index_less(p,primes):
    a = solution(p)
    i = math.floor(a/math.log(a))
    if less(p,primes[i]):
        while less(p,primes[i]):
            i += 1
        return i - 1
    return 0

primes = all_primes_below_n(16*10**6)
x = 0
hybrid = 0
for i in range(10**6):
    p = primes[i]
    index = index_less(p,primes)
    if primes[index] < p + 1:
        print(hybrid,"www")
        break
    hybrid += index - i

#answer = 1412403576
#זמן הרצה - שתי דקות