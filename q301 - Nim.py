def fib(k):
    if k == 1 or k == 2:
        return 1
    else:
        return fib(k-1) + fib(k-2)

x = 1
for k in range(1,31):
    x += fib(k)
print(x)

#answer = 2178309