import math

def log(x,y):
    return math.floor(math.log(y,x))

def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for k in range(3,int(math.sqrt(n))+1,2):
        if n % k == 0:
            return False
    return True

def hamming(limit,primes):
    list = []
    if limit == 1:
        return list
    if len(primes) == 1:
        for k in range(log(primes[0],limit) + 1):
            list.append(primes[0]**k)
        return list

    for k in range(log(primes[0],limit) + 1):
        lst = hamming(limit / primes[0]**k,primes[1:])
        for n in lst:
            list.append(n*primes[0]**k)
    return list

def mult_list(list1):
    m = 1
    for k in list1:
        m *= k
    return m

primes = [2,3,5,7,11,13,17,19,23]
admissible = []
for i in range(1,10):
    m = mult_list(primes[:i])
    lst = hamming(10**9/m,primes[:i])
    for h in lst:
        admissible.append(m*h)

m_list = []
for a in admissible:
    m = 2
    while not is_prime(a + m):
        m += 1
    m_list.append(m)

print(sum(list(dict.fromkeys(m_list))))

#Answer = 2209

