import math

def prime_factors(n,primes_list = [],m = 2):
    if n == 1:
        return primes_list
    if n % 2 == 0:
        return prime_factors(n // 2,primes_list + [2])
    else:
        if m == 2:
            m = 3
        for k in range(m,int(math.sqrt(n)) + 1,2):
            if n % k == 0:
                return prime_factors(n // k,primes_list + [k],m)
        return primes_list + [n]

def gcd(x,y):
    while x % y != 0:
        a = x
        b = y
        y = a % b
        x = b
    return y

def extended_Euclid(n,mod):
    if n < mod:
        return extended_Euclid(mod,n)[::-1]
    while n % mod != 0:
        i = extended_Euclid(mod,n % mod)
        q = n // mod
        return (i[1],i[0] - q*i[1])
    return (0,1)

def inverse(n,mod):
    return extended_Euclid(n,mod)[0] % mod

def phi(n):
    m = n
    for p in list(dict.fromkeys(prime_factors(n))):
        m = m*(p - 1) // p
    return m

def g(a,n,b,m):
    g1 = gcd(n,m)
    if (b - a) % g1 == 0:
        return (a + n*inverse(n // g1,m // g1)*(b - a) // g1) % (n*m // g1)
    return 0

phi_list = []
for i in range(5000):
    phi_list.append(phi(1000000 + i))

s = 0
for m in range(1,5000):
    for n in range(m):
        s += g(phi_list[n],1000000 + n,phi_list[m],1000000 + m)

print(s)

#Answer = 4515432351156203105