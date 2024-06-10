import math
def prime_factors_without_repetitions(n,primes_list): #בעת הקריאה לפונקציה יש להוסיף [] במקום של ה primes_list
    if n % 2 == 0:                                    #אחרת בהפעלה חוזרת הפונקציה לא תפעל
        if 2 not in primes_list:
            primes_list.append(2)
        return prime_factors_without_repetitions(n // 2, primes_list)
    if n == 1:
        return primes_list
    else:
        for k in range(3, int(math.sqrt(n)) + 1, 2):
            if n % k == 0:
                if k not in primes_list:
                    primes_list.append(k)
                return prime_factors_without_repetitions(n // k, primes_list)
    if n not in primes_list:
        primes_list.append(n)
    return primes_list

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

def euler_function(n):
    mult = n
    list = prime_factors_without_repetitions(n,[])
    for num in list:
        mult *= (1 - 1/num)
    return math.floor(mult)

def chain(n,len1 = 0):
    if n == 1:
        return len1 + 1
    elif len1 > 24:
        return 25
    return chain(euler_function(n),len1 + 1)

primes = all_primes_below_n(4*10**7)
x = 0
for p in primes:
    if chain(p - 1) == 24:
        x += p
print(x)

#answer = 1677366278943
