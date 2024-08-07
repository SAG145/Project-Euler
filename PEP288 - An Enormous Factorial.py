def t(p,q):
    s_list = [290797]
    t_list = []
    for n in range(q + 1):
        t_list.append(s_list[-1] % p)
        s_list.append(s_list[-1]**2 % 50515093)
    return t_list

def NF(p,q,mod):
    p_powers = [1]
    p_powers_sums = [1]
    for i in range(q + 3):
        p_powers.append(p_powers[-1]*p % mod)
    for i in range(1,q + 3):
        p_powers_sums.append((p_powers_sums[-1] + p_powers[i]) % mod)
    tn = t(p,q)
    factors_p = 0
    for n in range(1,q + 1):
        if tn[n] != 0:
            factors_p = (factors_p + tn[n]*p_powers_sums[n - 1]) % mod
    return factors_p

print(NF(61,10**7,61**10))

#answer = 605857431263981935
