def right_rotate(n):
    s = str(n)
    return int(s[-1] + s[:-1])

def property(n):
    return right_rotate(n) % n == 0

def same_digits(n):
    s = str(n)
    return s[0]*len(s) == s

def parasitic(n,k):
    mod = 10
    sk = k
    while not(property(k) and not same_digits(k)):
        k = 10*(n*k % mod) + sk
        mod *= 10
    return k

s = 0
for n in range(2,10):
    for k in range(n,10):
        x = str(parasitic(n,k))
        for m in range(1,100 // len(x) + 1):
            s += int(m*x)

for d in range(1,10):
    for l in range(2,101):
        s += int(str(d)*l)

print(s % 10**5)

#Answer = 59206
