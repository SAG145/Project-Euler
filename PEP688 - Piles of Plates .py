def tri(n):
    return n*(n + 1) // 2

def S(n):
    s = 0
    k = 1
    while True:
        t = tri(k)
        if t > n:
            break
        m = (n - t + k) // k - 1
        s += tri(m)*k
        s += (m + 1)*((n - t) % k + 1)
        s %= 10**9 + 7
        k += 1
    return s

print(S(10**16))

#Answer = 110941813
#Time: 3:00
