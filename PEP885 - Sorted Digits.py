from math import factorial

def factorial_list(lst):
    m = 1
    for i in lst:
        m *= factorial(i)
    return m

def digits_to_num(digits):
    n = "0"
    for d in range(10):
        n += str(d)*digits[d]
    return int(n)

def S(n):
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
                                        x = (x + digits_to_num(digits)*factorial(n) // factorial_list(digits)) % 1123455689
    return x

print(S(18))

#Answer = 827850196

