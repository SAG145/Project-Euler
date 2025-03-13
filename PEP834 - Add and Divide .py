import math

def all_min_pf_below_n(n):
    min_pf = [0]*n
    for k in range(2,int(math.sqrt(n)) + 1):
        if min_pf[k] == 0:
            for l in range(2*k,n,k):
                if min_pf[l] == 0:
                    min_pf[l] = k
    return min_pf

def all_prime_factorisations_below_n(n):
    min_pf = all_min_pf_below_n(n)
    pf = [0,[]]
    for k in range(2,n):
        mpf = min_pf[k]
        if mpf == 0:
            pf.append((k,))
        else:
            pf.append(pf[k // mpf] + (mpf,))
    return pf

def shortened_pf(pf):
    spf = []
    i = 1
    p = pf[0]
    pp = 1
    while i < len(pf) + 1:
        if i == len(pf) or pf[i] != p:
            spf.append((p,pp))
            if i != len(pf):
                p = pf[i]
                pp = 1
        else:
            pp += 1
        i += 1
    return spf

def merge_sorted_lists(lst1,lst2):
    new = []
    i = 0
    j = 0
    while i != len(lst1) or j != len(lst2):
        if i == len(lst1):
            new += lst2[j:]
            j = len(lst2)
        elif j == len(lst2):
            new += lst1[i:]
            i = len(lst1)
        elif lst1[i] < lst2[j]:
            new.append(lst1[i])
            i += 1
        else:
            new.append(lst2[j])
            j += 1
    return new

def divisors(divi,pf,pre = 0,curr = 1,i = 0):
    if pre != 0:
        divi.append(curr)
    if i < len(pf):
        a = 1
        for power in range(pf[i][1] + 1):
            divisors(divi,pf,power,curr*a,i + 1)
            a *= pf[i][0]

def T(pf1,pf2,mini):
    pf = merge_sorted_lists(pf1[::-1],pf2[::-1])
    divi = []
    divisors(divi,shortened_pf(pf))
    s = 0
    for d in divi:
        d -= mini
        if d > 0 and (mini + mini*d + d*(d + 1) // 2) % (d + mini) == 0:
            s += d
    return s

def U(N):
    s = 0
    apf = all_prime_factorisations_below_n(N + 1)
    for n in range(3,N + 1):
        s += T(apf[n],apf[n - 1],n)
    return s

print(U(1234567))

#Answer = 1254404167198752370
#Time: 2:30

