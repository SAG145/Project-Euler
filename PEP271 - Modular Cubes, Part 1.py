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

def solution(a,n,mod):
    return mod // n*inverse(inverse(a,n)*mod // n,n) % mod

def chinese_reminder(a,n,b,m):
    return (solution(a,n,n*m) + solution(b,m,n*m)) % (n*m)

def base_C(p):
    s = []
    for k in range(p):
        if k**3 % p == 1:
            s.append(k)
    return s

def C(solutions,primes,mod):
    if len(primes) == 0:
        return sum(solutions) - 1
    if len(solutions) == 0:
        return C(base_C(primes[0]),primes[1:],primes[0])
    new = []
    for k in base_C(primes[0]):
        for sol in solutions:
            new.append(chinese_reminder(sol,mod,k,primes[0]))
    return C(new,primes[1:],mod*primes[0])

print(C([],[2,3,5,7,11,13,17,19,23,29,31,37,41,43],1))

#answer = 4617456485273129588