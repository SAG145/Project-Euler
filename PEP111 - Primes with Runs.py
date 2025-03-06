import math
import copy

def insert(k,lst):
    new = []
    lst1 = (k,)
    for i in range(len(lst)):
        new.append(lst[:i] + lst1 + lst[i:])
    new.append(lst + lst1)
    return new

def permutations(lst):
    if len(lst) == 1:
        return [(lst[0],)]
    else:
        perm_list = []
        list1 = permutations(lst[1:])
        for perm in list1:
            perm_list += insert(lst[0],perm)
        return perm_list

def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for k in range(3,int(math.sqrt(n))+1,2):
        if n % k == 0:
            return False
    return True

power_lst = [1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000]
def tuple_to_number(t):
    num = 0
    l = len(t)
    t = t[::-1]
    for i in range(l):
        num += t[i]*power_lst[i]
    return num

def M(n,d):
    for k in range(1,n):
        lst = []
        for j in range(n - k):
            lst.append(d)
        for i in range(10**(k - 1),10**k):
            if str(d) not in str(i):
                digits = copy.copy(lst)
                a = i
                while a > 0:
                    digits.append(a % 10)
                    a = a // 10
                if sum(digits) % 3 != 0:
                    options = list(dict.fromkeys(permutations(digits)))
                    for tup in options:
                        if tup[0] != 0:
                            if is_prime(tuple_to_number(tup)):
                                return n - k

def S(n,d):
    m = M(n,d)
    primes = []
    sum1 = 0
    lst = []
    for k in range(m):
        lst.append(d)
    for i in range(10**(n - m - 1),10**(n - m)):
        if str(d) not in str(i):
            digits = copy.copy(lst)
            a = i
            while a > 0:
                digits.append(a % 10)
                a = a // 10
            if sum(digits) % 3 != 0:
                options = list(dict.fromkeys(permutations(digits)))
                for tup in options:
                    if tup[0] != 0:
                        num = tuple_to_number(tup)
                        if is_prime(num) and num not in primes:
                            sum1 += num
                            primes.append(num)
    return sum1

x = 0
for d in range(10):
    x += S(10,d)
print(x)

#answer = 612407567715
#7 minutes and 30 seconds.
#TThe code was changed a bit after solving the problem because the original solution used a library.
