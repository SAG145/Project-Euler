def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
i = 1
x = 0
while fib(i)<4000000:
    if fib(i)%2==0:
        x += fib(i)
    i +=1
print(x)
# answer = 4613732
