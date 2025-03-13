import math

def squarefree(limit,mobius):
    squarefree_numbers = limit
    for i in range(2,math.isqrt(limit) + 1):
        if mobius[i] == 1:
            squarefree_numbers += limit // i**2
        elif mobius[i] == -1 or mobius[i] == "":
            squarefree_numbers -= limit // i**2
    return squarefree_numbers

limit = 10**16
num_of_pf = [0]*(math.isqrt(limit) + 1)
n_list = [0]*(math.isqrt(limit) + 1)
for p in range(2,math.isqrt(math.isqrt(limit)) + 1):
    if num_of_pf[p] == 0:
        for i in range(p,len(num_of_pf),p):
            num_of_pf[i] += 1
            if n_list[i] == 0:
                n_list[i] = i
            while n_list[i] % p == 0:
                n_list[i] //= p
for j in range(2,len(num_of_pf)):
    if n_list[j] != 1:
        num_of_pf[j] += 1

mobius = [""]*(math.isqrt(limit) + 1)
for p in range(2,math.isqrt(limit) + 1):
    if mobius[p] == "":
        squ = 1
        for t in range(p,math.isqrt(limit) + 1,p):
            if mobius[t] == "":
                mobius[t] = -1
            else:
                mobius[t] *= -1
            if squ == 0:
                mobius[t] = 0
            squ += 1
            if squ == p:
                squ = 0

ckn_list = [0]*50
ckn_list[0] = squarefree(limit,mobius)
for n in range(2,len(num_of_pf)):
    ckn_list[num_of_pf[n]] += squarefree(limit // n**2,mobius)

m = ckn_list[0]
l = 1
while ckn_list[l] != 0:
    m *= ckn_list[l]
    l += 1

print(m % (10**9 + 7))

#Answer = 728378714
#Time: 12:30
