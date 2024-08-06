import math
def pitagoras(a,b):
    c = int(math.sqrt(a**2+b**2))
    if a**2 + b**2 == c**2:
        return [True,c]
    else:
        return [False,999]

x = - 1
for p in range(12,1001):
    lst = []
    for k in range(1,p):
        for l in range(1,p-1):
            y = pitagoras(k,l)
            if y[0] == True:
                if k + l + y[1] == p:
                    lst.append((k,l))
    if len(lst)/2 > x:
        x = int(len(lst)/2)
print(x)
#answer = 840
