import math

def num_of_square_free(limit,mobius):
    squarefree_numbers = limit
    for i in range(2,math.isqrt(limit) + 1):
        if mobius[i] == 1:
            squarefree_numbers += limit // i ** 2
        elif mobius[i] == -1 or mobius[i] == "":
            squarefree_numbers -= limit // i ** 2
    return squarefree_numbers

def S(N):
    mobius = [""] * (math.isqrt(N) + 1)
    for p in range(2,math.isqrt(N) + 1):
        if mobius[p] == "":
            squ = 1
            for t in range(p, math.isqrt(N) + 1, p):
                if mobius[t] == "":
                    mobius[t] = -1
                else:
                    mobius[t] *= -1
                if squ == 0:
                    mobius[t] = 0
                squ += 1
                if squ == p:
                    squ = 0

    sigma = 0
    for k in range(1,math.isqrt(N) + 1):
        sigma += k**2*(num_of_square_free(N // k**2,mobius))
    return sigma

print(S(10**14) % (10**9 + 7))

#Answer = 94586478
