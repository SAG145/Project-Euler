import math

def digits_sum(n):
    s = 0
    for c in str(n):
        s += int(c)
    return s

def drs(n,drs_list):
    x = drs_list[digits_sum(n)]
    drs_list.append(x)

def mdrs(n,mdrs_list,drs_list):
    m = drs_list[n]
    for d in range(2,math.isqrt(n) + 1):
        if n % d == 0:
            m = max(m,mdrs_list[d] + mdrs_list[n // d])
    mdrs_list.append(m)

drs_list = [0,1,2,3,4,5,6,7,8,9]
for k in range(10,10**6):
    drs(k,drs_list)

mdrs_list = [0,0,2,3,4,5,6,7,8,9]
for k in range(10,10**6):
    mdrs(k,mdrs_list,drs_list)

print(sum(mdrs_list))

#Answer = 14489159

