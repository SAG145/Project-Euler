import math
def prime_factors_with_repetitions(n,primes_list = [],m = 2):
    if n % 2 == 0:
        return prime_factors_with_repetitions(n // 2,primes_list + [2])
    else:
        if m == 2:
            m = 3
        for k in range(m,int(math.sqrt(n)) + 1,2):
            if n % k == 0:
                return prime_factors_with_repetitions(n // k,primes_list + [k],m)
        return primes_list + [n]

def multiple_list(lst):
    m = 1
    for k in lst:
        m *= k
    return m

def disjoint(list1,list2,list3 = []):
    lists = list1  + list2 + list3
    return list(dict.fromkeys(lists)) == lists

def sigma_c(maxi):
    max_p = maxi // 30 + 1
    options = []
    rad_nums = [0,1]
    rad_factors = [0,[]]
    rad_nums_options = []
    for n in range(2,maxi):
        pf = prime_factors_with_repetitions(n)
        rad_pf = list(dict.fromkeys(pf))
        rad_n = multiple_list(rad_pf)
        if n != rad_n and rad_pf[-1] < max_p:
            options.append(n)
            rad_nums_options.append(rad_n)
        rad_nums.append(rad_n)
        rad_factors.append(rad_pf)
    rad_nums_options = list(dict.fromkeys(rad_nums_options))
    coprime_rad = [0]*maxi
    v = 0
    for r in rad_nums_options:
        coprimes = []
        pf = rad_factors[r]
        for k in range(1,rad_nums[r]):
            if disjoint(pf,rad_factors[k]):
                coprimes.append(k)
        coprime_rad[rad_nums[r]] = coprimes
        v += 1
    sum_of_c = 0
    for c in options:
        for cop in coprime_rad[rad_nums[c]]:
            for m in range(c):
                a = cop + m*rad_nums[c]
                if 2*a > c - 1:
                    break
                if disjoint(rad_factors[c],rad_factors[a],rad_factors[c - a]):
                    if rad_nums[a]*rad_nums[c]*rad_nums[c - a] < c:
                        sum_of_c += c
    return sum_of_c

print(sigma_c(120000))

#answer = 18407904
#זמן הרצה = 21 דקות