import math
def fib(n):
    f1 = 0
    f2 = 1
    f3 = 0
    for i in range(n):
        a = f2
        f1 = f2
        f2 = f3
        f3 += a
    return f3
for i in range(10000):
    if len(str(fib(i)))>999:
        print(i)
        break
#answer = 4782