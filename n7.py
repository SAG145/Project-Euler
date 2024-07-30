import math
fib = [0,1,1]
for k in range(1000):
    fib.append(fib[-1] + fib[-2])

def AF(x):
    s = 0
    for i in range(1,1000):
        s += x**i*fib[i]
    return s

def sol_to_int(target):
    x = 0
    for p in range(1,20):
        change = False
        for d in range(10):
            if AF(x + d*10**-p) > target:
                change = True
                x += (d - 1)*10**-p
                break
        if not change:
            x += 9*10**-p
    return x

def func(p,q):
    print(AF(p / q),p*q)
    return p*q / AF(p / q)

# print(fib[:20])
# x = (math.sqrt(377) - 13) / 21
# print(AF(x))
# for k in range(1,math.isqrt(74049690) + 1):
#     if 74049690 % k == 0:
#         print(func(k,74049690 // k),"ooo")

print(func(29,47))