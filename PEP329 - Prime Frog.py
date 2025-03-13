import math
from fractions import Fraction

def all_primes_below_n(n):
    primes_bool = [False, False] + [True] * (n - 2)
    for k in range(2, int(math.sqrt(n)) + 1):
        if primes_bool[k]:
            for l in range(2*k,n,k):
                primes_bool[l] = False
    primes = []
    for p in primes_bool:
        if p:
            primes.append("P")
        else:
            primes.append("N")
    return primes

def all_jumps(prob,primes,target,square_primes,jumps,poss,prob_jumps):
    square_primes += primes[poss]
    if len(jumps) == 14:
        chance = Fraction(1,prob_jumps*3**15)
        for i in range(15):
            if square_primes[i] == target[i]:
                chance *= 2
        prob[0] += chance
    else:
        if poss == 500:
            all_jumps(prob,primes,target,square_primes,jumps + "l",poss - 1,prob_jumps)
        elif poss == 1:
            all_jumps(prob,primes,target,square_primes,jumps + "r",poss + 1,prob_jumps)
        else:
            all_jumps(prob,primes,target,square_primes,jumps + "l",poss - 1,prob_jumps*2)
            all_jumps(prob,primes,target,square_primes,jumps + "r",poss + 1,prob_jumps*2)

primes = all_primes_below_n(501)
prob = [Fraction(0,1)]
for start_poss in range(1,501):
    print(start_poss)
    all_jumps(prob, primes, "PPPPNNPPPNPPNPN", "", "", start_poss, 500)

print(prob[0])

#Answer = 199740353/29386561536000

#Time: 2:00
