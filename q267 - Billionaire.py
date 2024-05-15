import math
factorial = []
for n in range(1001):
    factorial.append(math.factorial(n))

def choose(n,k):
    return factorial[n] // factorial[k] // factorial[n - k]

def chance_to_billion(i):
    s = 0
    if i < 500:
        for k in range(i):
            s += choose(1000, k)
        return (2**1000 - s) / 2**1000
    elif i == 1001:
        return 0
    else:
        for k in range(i, 1001):
            s += choose(1000, k)
        return s / 2 ** 1000
def exist_f(min_wins):
    for x in range(1,100):
        f = x / 100
        if min_wins*math.log(1 + 2*f,10) + (1000 - min_wins)*math.log(1 - f,10) > 9:
            return True
    return False

for i in range(1,1001):
    if exist_f(i):
        print(round(10**12*chance_to_billion(i)) / 10**12)
        break

#answer = 0.999992836187