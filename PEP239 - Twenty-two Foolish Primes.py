from math import comb, factorial

def deploy(m,n):
    if n == 1:
        return m - 1
    if m == 1:
        return 1
    if m == n:
        d = factorial(m)
        for i in range(1,m + 1):
            d += (-1)**i*comb(m,i)*factorial(m - i)
        return d
    d = 0
    for j in range(max(0,2*n - m),n + 1):
        d += comb(n,j)*deploy(n,j)*factorial(m - n) // factorial(m - 2*n + j)
    return d

print(round(comb(25,3)*deploy(97,22)*factorial(75) / factorial(100),12))