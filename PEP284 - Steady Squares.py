import math
import sys
sys.setrecursionlimit(10**4)
def extended_Euclid(n,mod):
    if n < mod:
        return extended_Euclid(mod,n)[::-1]
    while n % mod != 0:
        i = extended_Euclid(mod, n % mod)
        q = n // mod
        return (i[1], i[0] - q * i[1])
    return (0, 1)

def inverse(n, mod):
    return extended_Euclid(n, mod)[0] % mod

def sum_base14(n, m):
    if len(n) > len(m):
        return sum_base14(m, n)
    n = [0] * (len(m) - len(n)) + n
    n = n[::-1]
    m = m[::-1]
    sum1 = []
    for i in range(len(n) - 1):
        sum1.append((n[i] + m[i]) % 14)
        n[i + 1] += (n[i] + m[i]) // 14
    sum1.append((n[-1] + m[-1]) % 14)
    if n[-1] + m[-1] >= 14:
        sum1.append(1)
    return sum1[::-1]

def digits_sum_base14(dec_n):
    ds = []
    while dec_n > 0:
        mp = 14**math.floor(math.log(dec_n,14))
        divi = dec_n // mp
        ds = sum_base14(ds,[divi])
        dec_n -= mp*divi
    return ds

def steady_squares_digits_sum(n):
    a = 7**n
    b = 2**n
    s1 = a*inverse(a, b)
    s2 = b*inverse(b, a)
    t = []
    if math.floor(math.log(s1,14)) == n - 1:
        t = sum_base14(t,digits_sum_base14(s1))
    if math.floor(math.log(s2,14)) == n - 1:
        t = sum_base14(t, digits_sum_base14(s2))
    return t

suma = [1]
for n in range(10**4,0,-1):
    suma = sum_base14(suma,steady_squares_digits_sum(n))

s = ""
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d"]
for d in suma:
    s += digits[d]

print(s)

#answer = 5a411d7b