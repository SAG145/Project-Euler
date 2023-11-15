def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def factorial_list(lst):
    mult = 1
    for n in lst:
        mult *= factorial(n)
    return mult

def S(k):
    x = 0
    for d0 in range(k):
        for d1 in range(k - d0 + 1):
            for d2 in range(k - d0 - d1 + 1):
                for d3 in range(k - d0 - d1 - d2 + 1):
                    for d4 in range(k - d0 - d1 - d2 - d3 + 1):
                        for d5 in range(k - d0 - d1 - d2 - d3 - d4 + 1):
                            for d6 in range(k - d0 - d1 - d2 - d3 - d4 - d5 + 1):
                                for d7 in range(k - d0 - d1 - d2 - d3 - d4 - d5 - d6 + 1):
                                    for d8 in range(k - d0 - d1 - d2 - d3 - d4 - d5 - d6 - d7 + 1):
                                        for d9 in range(k - d0 - d1 - d2 - d3 - d4 - d5 - d6 - d7 - d8 + 1):
                                            if d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 == k:
                                                digits = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9]
                                                permutation = factorial(k) // factorial_list(digits) * (k - d0) // k
                                                x += permutation * (permutation - 1) // 2
    return int(x)
print(S(12))

#answer = 6111397420935766740