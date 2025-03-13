def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def factorial_list(lst):
    mult = 1
    for n in lst:
        mult *= factorial(n)
    return mult

permutations = 0
for d0 in range(4):
    for d1 in range(4):
        for d2 in range(4):
            for d3 in range(4):
                for d4 in range(4):
                    for d5 in range(4):
                        for d6 in range(4):
                            for d7 in range(4):
                                for d8 in range(4):
                                    for d9 in range(4):
                                        if d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 == 18:
                                            digits = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9]
                                            permutations += factorial(18) // factorial_list(digits) * (18 - d0) // 18
print(permutations)

#Answer = 227485267000992000

