def u(k,r):
    return (900 - 3*k)*r**(k-1)

def s(r):
    sum = 0
    for k in range(1,5001):
        sum += u(k,r)
    return sum

guess = 0
power = 0
while power > -15:
    for k in range(10):
        if s(guess + k*10**power) < -600000000000:
            guess += (k-1)*10**power
            power -= 1
            break
print(round(10**12*guess) / 10**12)

#Answer = 1.002322108633

