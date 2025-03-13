import math

limit = 2**50
mobius = [""]*(math.isqrt(limit) + 1)
for p in range(2,math.isqrt(limit) + 1):
    if mobius[p] == "":
        squ = 1
        for t in range(p,math.isqrt(limit) + 1,p):
            if mobius[t] == "":
                mobius[t] = -1
            else:
                mobius[t] *= -1
            if squ == 0:
                mobius[t] = 0
            squ += 1
            if squ == p:
                squ = 0

squarefree_numbers = limit
for i in range(2,len(mobius)):
    if mobius[i] == 1:
        squarefree_numbers += limit // i**2
    elif mobius[i] == -1 or mobius[i] == "":
        squarefree_numbers -= limit // i**2

print(squarefree_numbers)

#Answer = 684465067343069

