import math

def all_primes_below_n(n):
    primes_bool = [True]*n
    for k in range(2, math.isqrt(n) + 1):
        if primes_bool[k]:
            for l in range(k**2,n,k):
                primes_bool[l] = False
    primes_list = []
    for k in range(2,n):
        if primes_bool[k]:
            primes_list.append(k)
    return primes_list

def mult(a,b):
    new = [a[0]*b[0],a[1] + b[1]]
    if new[0] > 10:
        new[0] /= 10
        new[1] += 1
    if new[0] < 1:
        new[0] *= 10
        new[1] -= 1
    return new

def round_phi_power(n):
    if n == 1:
        return [(1 + math.sqrt(5)) / 2,0]
    k = round_phi_power(n // 2)
    m = mult(k,k)
    if n % 2 == 1:
        m = mult(m,[(1 + math.sqrt(5)) / 2,0])
    return m

def alpha(p):
    a = 1
    b = 1
    n = 2
    while b != 0 and n < 14*10**7 // p:
        b = (a + b) % p
        a = (b - a) % p
        n += 1
    if b == 0:
        return n
    return 0


lst = []
for p in all_primes_below_n(10**7):
    lst.append(p*alpha(p))

lst.sort()

new = lst
for i in range(len(lst) - 1):
    if new[i] != 0:
        for j in range(i + 1,len(new)):
            if new[j] % new[i] == 0:
                new[j] = 0

new = list(dict.fromkeys(new))
new.sort()
new.remove(0)


square_free = [True]*(14*10**7)
for n in new:
    for i in range(n,len(square_free),n):
        square_free[i] = False
f = 0
for i in range(1,len(square_free)):
    if square_free[i]:
        f += 1
        if f == 10**8:
            break

a = 1
b = 1
mod = 10**16
for _ in range(3,i + 1):
    b = (a + b) % mod
    a = (b - a) % mod
fib = mult(round_phi_power(i),[1 / math.sqrt(5),0])
print(str(b) + "," + str(round(fib[0],1)) + "e" + str(fib[1]))

#Answer = 1508395636674243,6.5e27330467