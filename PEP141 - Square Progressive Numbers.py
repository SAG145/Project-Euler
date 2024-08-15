import math
def perfect_square(n):
    return math.isqrt(n)**2 == n

def rec_prime_factors(prime_factors,n):
    if n == 2:
        return (2,)
    if n % 2 == 0:
        return prime_factors[n // 2] + (2,)
    for k in range(3,int(math.sqrt(n)) + 1,2):
        if n % k == 0:
            return prime_factors[n // k] + (k,)
    return (n,)

def divisors(divi,pf,d = 1,i = 0):
    if i == len(pf):
        divi.append(d)
    else:
        for pow in range(pf[i][1] + 1):
            divisors(divi,pf,d*pf[i][0]**pow,i + 1)

def square_divisors(pf):
    pf_powers_squ = []
    distinct_pf = tuple(dict.fromkeys(pf))
    for dpf in distinct_pf:
        pf_powers_squ.append([dpf,0])
    for p in pf:
        pf_powers_squ[distinct_pf.index(p)][1] += 2
    divi = []
    divisors(divi,pf_powers_squ)
    return sorted(divi)[::-1]

prime_factors = [(0,),(1,)]
for n in range(2,10**6):
    prime_factors.append(rec_prime_factors(prime_factors,n))

progressive_squares = [False]*10**6
limit = 10**12
for d in range(2,10**6):
    divi = square_divisors(prime_factors[d])
    for q in divi:
        if q <= d:
            break
        n = q*d + d**2 // q
        if perfect_square(n) and n < limit:
            progressive_squares[math.isqrt(n)] = True

sum_prog_squ = 0
for i in range(len(progressive_squares)):
    if progressive_squares[i]:
        sum_prog_squ += i**2

print(sum_prog_squ)

#answer = 878454337159