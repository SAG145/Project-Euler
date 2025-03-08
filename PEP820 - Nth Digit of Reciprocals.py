def d(n,k):
    return int(10*pow(10,n - 1,k) / k)

def S(n):
    s = 0
    for k in range(1,n + 1):
        s += d(n,k)
    return s

print(S(10**7))

#answer = 44967734
