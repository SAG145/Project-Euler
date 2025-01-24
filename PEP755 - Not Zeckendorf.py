def s(fib,n,fi):
    if n >= fib[fi + 2] - 2:
        return 2**(fi - 1)
    if n == 0:
        return 1
    t = 1
    i = 1
    while i < fi and fib[fi] + fib[i] <= n:
        t += s(fib,n - fib[fi],i)
        i += 1
    return t

def S(n):
    fib = [0,1,2]
    for _ in range(100):
        fib.append(fib[-1] + fib[-2])
    t = 1
    fi = 1
    while fib[fi] <= n:
        t += s(fib,n,fi)
        fi += 1
    return t

print(S(10**13))

#answer = 2877071595975576960