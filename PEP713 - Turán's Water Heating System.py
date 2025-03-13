def c2(n):
    return n*(n - 1) // 2

def T(N,m):
    if m == 2:
        return c2(N)
    a = N // (m - 1)
    b = N % (m - 1)
    return b*c2(a + 1) + (m - b - 1)*c2(a)

def L(N):
    s = 0
    for m in range(2,N + 1):
        s += T(N,m)
    return s

print(L(10**7))

#Answer = 788626351539895

