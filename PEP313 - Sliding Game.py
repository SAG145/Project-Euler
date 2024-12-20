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

grids = 6
for p in all_primes_below_n(10**6)[2:]:
    s = (p**2 + 3) // 4 + 2
    grids += s - 3
print(grids // 3)

#answer = 2057774861813004
#לא ברור למה הקוד עובד
