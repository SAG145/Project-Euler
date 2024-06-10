import math
def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for k in range(3,int(math.sqrt(n))+1,2):
        if n % k == 0:
            return False
    return True

def prime_factors_with_repetitions(n,primes_list):
    if n % 2 == 0:
        primes_list.append(2)
        return prime_factors_with_repetitions(n//2,primes_list)
    elif is_prime(n):
        primes_list.append(int(n))
        return primes_list
    else:
        for k in range(3,int(math.sqrt(n))+1,2):
            if n % k == 0:
                if is_prime(k):
                    primes_list.append(k)
                    return prime_factors_with_repetitions(n//k,primes_list)

def fib(n,values,index):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif index[-1] >= n-1:
        return values[n-1] + values[n-2]
    else:
        return fib(n-1) + fib(n-2)

def period_len(list1):
    len1 = len(list1)
    period_list = []
    for k in range(len1):
        current_period = list1[k:k+120]
        if current_period in period_list:
            return k - period_list.index(current_period)
        period_list.append(current_period)
    return 0
values = [0,1,1]
index = [1,2]
for k in range(3,1801):
    values.append(fib(k,values,index))
    index.append(k)

# for k in range(121,241):
#     d = values[k] - values[k-120]
#     # print(values[k],values[k-120])
#     if d % (16*9*5*11*31*41*61*2521) != 0:
#         print(k,k-120,d,"\n")
#         break
#     print(k,d,prime_factors_with_repetitions(d,[]))

a = 16*9*5*11*31*41*61*2521 # מוצאים את a דרך הרצה של הלולאה

def divisors(n):
    list1 = []
    for k in range(2,int(math.sqrt(n))+1):
        if n % k == 0:
            if k < 10**9:
                list1.append(k)
            if n/k < 10**9:
                list1.append(n//k)
    return list1

divisors_a = divisors(a)
x = 0
for d in divisors_a:
    pi_d = []
    for f in values:
        pi_d.append(f % d)
    if period_len(pi_d) == 120:
        x += d
print(x)

#answer = 44511058204
