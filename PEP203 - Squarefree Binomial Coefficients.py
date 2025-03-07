import math
from math import factorial

def choose(n,k):
    return factorial(n)//factorial(k)//factorial(n-k)

def is_squarefree(n):
    rt = math.floor(n**(1/4))
    if n % 2 != 0:
        for k in range(3,rt + 10, 2):
            if n % (k ** 2) == 0:
                return False
                
    else:
        for k in range(2, rt + 10):
            if n % (k ** 2) == 0:
                return False
    return True

def is_square(n):
    return math.floor(math.sqrt(n))**2 == n

pascal = [1]
for n in range(2,51):
    for k in range(1,n // 2 + 1):
        c = choose(n,k)
        if is_squarefree(c) and not is_square(c):
            pascal.append(c)

pascal = list(dict.fromkeys(pascal))
print(sum(pascal))

#answer = 34029210557338
