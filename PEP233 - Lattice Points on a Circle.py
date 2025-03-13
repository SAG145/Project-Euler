import math

def max_power_divides(n,p):
    power = 0
    while n % p == 0:
        n //= p
        power += 1
    return power

def all_primes_below_n(n):
    primes_bool = [True]*n
    for k in range(2,math.isqrt(n) + 1):
        if primes_bool[k]:
            for l in range(k**2,n,k):
                primes_bool[l] = False
    primes_list = []
    for k in range(2,n):
        if primes_bool[k]:
            primes_list.append(k)
    return primes_list

def sum_of_nums(limit,primes,neut_sums,powers):
    s = 0
    i = 0
    while primes[i]**powers[0] <= limit:
        j = 0
        a = primes[i]**powers[0]
        while a*primes[j]**powers[1] <= limit:
            if i != j:
                b = a*primes[j]**powers[1]
                if len(powers) == 3:
                    k = 0
                    while b*primes[k]**powers[2] <= limit:
                        if i != k and j != k:
                            c = b*primes[k]**powers[2]
                            s += c*neut_sums[limit // c]
                        k += 1
                else:
                    s += b*neut_sums[limit // b]
            j += 1
        i += 1
    return s

ap = all_primes_below_n(5*10**6)
primes = []
neutrals = [True]*5*10**6
for p in ap:
    if p % 4 == 1:
        primes.append(p)
        for i in range(p,len(neutrals),p):
            neutrals[i] = False

neut_sums = [0]
for i in range(1,5*10**6):
    neut_sums.append(neut_sums[-1])
    if neutrals[i]:
        neut_sums[-1] += i

all_powers = [[3,2,1],[7,3],[10,2]]
x = 0
for powers in all_powers:
    x += sum_of_nums(10**11,primes,neut_sums,powers)

print(x)

#Answer = 271204031455541309
