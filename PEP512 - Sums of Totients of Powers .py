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

def euler_function(n):
    mult = n
    pf = list(dict.fromkeys(prime_factors(n)))
    for p in pf:
        mult = mult*(p - 1) // p
    return mult

def summatory_totient(n,slist):
    if n < len(slist) and slist[n] != 0:
        return slist[n]
    s = n*(n + 1) // 2
    for m in range(2,math.isqrt(n) + 1):
        s -= summatory_totient(n // m,slist)
    for d in range(1,math.isqrt(n) + 1):
        if d != n // d:
            s -= (n // d - n // (d + 1))*summatory_totient(d,slist)
    if n < len(slist):
        slist[n] = s
    return s

def s_tot_even(n,s_list,se_list):
    if n < len(se_list) and se_list[n] != 0:
        return se_list[n]
    if n % 2 != 0:
        ste = s_tot_even(n - 1,s_list,se_list)
        se_list[n] = ste
        return ste
    ste = s_tot_odd(n // 2,s_list,se_list) + 2*s_tot_even(n // 2,s_list,se_list)
    if n < len(se_list):
        se_list[n] = ste
    return ste

def s_tot_odd(n,s_list,se_list):
    return summatory_totient(n,s_list) - s_tot_even(n,s_list,se_list)

slist = [0]*(25*10**7 + 10)
for k in range(1,100):
    slist[k] = euler_function(k) + slist[k - 1]

se_list = [0]*(25*10**7 + 10)
se_list[2] = 1

print(s_tot_odd(5*10**8,slist,se_list))

#Answer = 50660591862310323

