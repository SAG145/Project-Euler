import math
import copy
def factorial_list(lst):
    m = 1
    for i in lst:
        m *= math.factorial(i)
    return m

def digits_to_num(digits):
    n = "0"
    for d in range(10):
        n += str(d)*digits[d]
    return int(n)

def f(digits):
    sum1 = 0
    for d in range(1,10):
        sum1 += digits[d]*d**2
    return sum1

def perfect_square(n):
    return math.floor(math.sqrt(n))**2 == n

def permutations(list):
    return math.factorial(sum(list)) // factorial_list(list)

def sum_of_all_permutations(digits):
    sum1 = 0
    a = int("1"*9)
    for i in range(10):
        if digits[i] != 0:
            ilst = copy.copy(digits)
            ilst[i] -= 1
            sum1 += permutations(ilst)*a*i
    return sum1

def sum_of_n(n):
    x = 0
    for a1 in range(n + 1):
        for a2 in range(n - a1 + 1):
            for a3 in range(n - a1 - a2 + 1):
                for a4 in range(n - a1 - a2 - a3 + 1):
                    for a5 in range(n - a1 - a2 - a3 - a4 + 1):
                        for a6 in range(n - a1 - a2 - a3 - a4 - a5 + 1):
                            for a7 in range(n - a1 - a2 - a3 - a4 - a5 - a6 + 1):
                                for a8 in range(n - a1 - a2 - a3 - a4 - a5 - a6 - a7 + 1):
                                    for a9 in range(n - a1 - a2 - a3 - a4 - a5 - a6 - a7 - a8 + 1):
                                        a0 = n - (a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9)
                                        digits = [a0,a1,a2,a3,a4,a5,a6,a7,a8,a9]
                                        if perfect_square(f(digits)):
                                            x = (x + sum_of_all_permutations(digits)) % 10**9
    return x

print(sum_of_n(20))

#answer = 142989277