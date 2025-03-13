import math

def father1(n):
    for i in range(100):
        if 2**i + 1 > n:
            return 2**(i - 1) + 1

def plus_list(lst,plus):
    new = []
    for k in lst:
        new.append(k + plus)
    return new

def path(n,k):
    if k == 1:
        f = father1(n)
        if f == n:
            return [f,1]
        return path(n,f) + [1]
    return plus_list(path(n - k + 1,1),k - 1)

print(sum(path(10**17,9**17)))

#Answer = 2903144925319290239
