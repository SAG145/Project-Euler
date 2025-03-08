def ston_dig(n,i):
    if 3**i > n:
        return 0
    return int(10*pow(10,n - 3**i - 1,3**i) / 3**i)

def A(n):
    s = 0
    for i in range(1,100):
        s1 = 0
        for j in range(100):
            s1 += ston_dig(n + j,i)
            s1 *= 10
        s1 //= 10
        s += s1
    return (s % 10**100) // 10**90

print(A(10**16))

#answer = 6086371427
