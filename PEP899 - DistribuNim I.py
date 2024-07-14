import math
def L(n):
    s = 0
    p = 2**math.floor(math.log(n,2)) - 1
    power_lists = []
    while p > 0:
        x = n // (p + 1) - sum(power_lists)
        power_lists.append(x)
        s += x*p
        p = (p - 1) // 2
    i = 1
    while bin(n)[-i] == "1":
        i += 1
    s += 2**(i - 1) - 1
    return 2*s - math.floor(math.log(n,2))

print(L(7**17))

#answer = 10784223938983273