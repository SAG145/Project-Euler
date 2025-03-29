import math

def all_totient(n):
    tots = [1]*(n + 1)
    for p in range(2,n + 1):
        if tots[p] == 1:
            for k in range(p,n + 1,p):
                if tots[k] == 1:
                    tots[k] = k
                tots[k] = (tots[k]*(p - 1)) // p
    return tots

def H(n):
    tots = all_totient(n)
    m = n // 2
    h = n - 1 + n // 2 - 1 + 1
    for i in range(1,n + 1):
        if i % 2 == 0:
            h += i - 2
            if i <= m:
                h -= 2*tots[i]
        else:
            h += 2*(i // 2 - tots[i] // 2)
            if i <= m:
                h -= tots[i]
    return 6*h

print(H(100000000))

#Answer = 11762187201804552

#Time: 2:00