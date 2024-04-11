import math
def all_primes_below_n(n):
    primes_bool = [False, False] + [True] * (n - 2)
    for k in range(2, int(math.sqrt(n)) + 1):
        if primes_bool[k]:
            for l in range(2*k,n,k):
                primes_bool[l] = False
    primes_list = []
    for k in range(n):
        if primes_bool[k]:
            primes_list.append(k)
    return primes_list

def min_add(factors):
    min_index = 0
    mini = factors[0][0]**(factors[0][1] + 1)
    for k in range(1,400): #400 זה בערך המיקום של הראשוני הכי גדול שהוא בריבוע יותר קטן מהראשוני ה 500500
        f = factors[k]
        if f[0]**(f[1] + 1) < mini:
            mini = f[0]**(f[1] + 1)
            min_index = k
    if factors[min_index][0]**2 > factors[-1][0] and factors[min_index][1] == 1:
        return -1
    return min_index

factors = []
for p in all_primes_below_n(10**7)[:500500]:
    factors.append((p,1))

while True:
    m = min_add(factors)
    if m == -1:
        break
    factors.pop(-1)
    factors[m] = (factors[m][0],2*factors[m][1] + 1)

num = 1
for f in factors:
    num = (num*f[0]**f[1]) % 500500507
print(num)

#answer = 35407281