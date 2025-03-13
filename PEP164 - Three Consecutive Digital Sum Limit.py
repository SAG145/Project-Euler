def digits_sum(n):
    ds = 0
    while n > 0:
        ds += n % 10
        n //= 10
    return ds

def next_digit(poss,opti_next_digits):
    new = [0]*100
    for num in range(100):
        if poss[num] != 0:
            for opti in opti_next_digits[num]:
                new[opti] += poss[num]
    return new

opti_next_digits = []
poss = []
for n in range(100):
    if digits_sum(n) > 9:
        opti_next_digits.append([])
        poss.append(0)
    else:
        next_dig = []
        d = n % 10
        for k in range(10  - digits_sum(n)):
            next_dig.append(10*d + k)
        if n > 9:
            poss.append(1)
        else:
            poss.append(0)
        opti_next_digits.append(next_dig)

for i in range(18):
    poss = next_digit(poss,opti_next_digits)
print(sum(poss))

#Answer = 378158756814587
#This code was written after the problem was solved because the original code was lost.

