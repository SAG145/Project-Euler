mod = 1000000007
# def s(n):
#     return int(str(n % 9) + "9"*(n//9))
#
# def base_s(n):
#     sum1 = 0
#     for k in range(1, n + 1):
#         sum1 = (sum1 + s(k)) % mod
#     return sum1
#
# lst = [(5,76),(7,75),(10,74),(14,73),(19,72),(25,71),(32,70),(40,69),(49,68)]
# def S(n):
#     l = n // 9
#     return (int(str(lst[n % 9][0]) + "9"*(l - 2) + str(lst[n % 9][1])) - 9*(l - 2)) % mod

tl = [60,80,11,15,20,26,33,41,50]
# def st(i):
#     return (10**((i - 2) // 9)*tl[i % 9] - i - 6) % mod

def S_fib(i):
    exp_10 = power_10_mod[i]
    f = values[i]
    return (exp_10*tl[f % 9] - f - 6) % mod

def fib(n,index,value_list):
    if n < index + 1:
        return value_list[n]
    else:
        return fib(n - 1,index,value_list) + fib(n - 2,index,value_list)

values = [0,1]
index = 1
for k in range(2,91):
    values.append(fib(k,index,values))
    index += 1

power_10_mod = [0,0,1,1,1,1,1]
for k in range(7,92):
    a = values[k - 1]
    b = values[k - 2]
    r = (2 + (a - 2) % 9 + (b - 2) % 9 - (a + b - 2) % 9) // 9
    power_10_mod.append((10**r*power_10_mod[-1]*power_10_mod[-2]) % mod)

x = -72
y = 0
z = 0
for k in range(2,91):
    x += S_fib(k)
print(x % mod)

#Answer = 922058210

#base_s is the simplest S (just like in the problem definition) from which I got to S, and from there easily to st, then fib_S is st with a clever calculation of the power of 10 with the modulo.
#Because of deviations to small values, x is initially equal to -72.
