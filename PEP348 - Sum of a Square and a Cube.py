import math

def pali(n):
    lst = []
    s = str(n)
    rs = s[::-1]
    lst.append(int(s + rs))
    for d in range(10):
        lst.append(int(s + str(d) + rs))
    return lst

def solutions_equal_4(n):
    sol = 0
    for k in range(2,math.floor(math.cbrt(n)) + 1):
        if math.isqrt(n - k**3)**2 == n - k**3:
            sol += 1
            if sol > 4:
                return False
    return sol == 4

solutions = []
k = 1
while len(solutions) != 5:
    for pal in pali(k):
        if solutions_equal_4(pal):
            solutions.append(pal)
    k += 1
print(sum(solutions))

#Answer = 1004195061

