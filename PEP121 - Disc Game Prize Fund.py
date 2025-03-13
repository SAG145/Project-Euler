def factorial(n):
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            mult = n*(n//2)
            for k in range(1,n//2):
                mult *= k*(n-k)
            return mult
        else:
            mult = n
            for k in range(1,n//2+1):
                mult *= k*(n-k)
            return mult

def choose(k,n):
    return factorial(n)//factorial(k)//factorial(n-k)

def func_7_15(k,x):
    if x == k:
        return factorial(k)
    elif k == 1:
        return x*(x + 1)//2
    else:
        return func_7_15(k,x-1) + x*func_7_15(k-1,x-1)

def win(discs):
    sum = 1
    for k in range(1,discs//2 + 1 - (discs + 1) % 2):
        sum += func_7_15(k,discs)
    return sum/factorial(discs + 1)

print(int(1/win(15)))

#Answer = 2269

