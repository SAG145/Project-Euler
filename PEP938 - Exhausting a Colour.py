def next(probs,B,r):
    new = [0]*(r + 1)
    new[0] = 1
    for R in range(2,len(new)):
        if R % 2 == 0:
            t = (R*(R - 1) / ((B + R)*(B + R - 1)))*new[R - 2]
            t += (2*B*R / ((B + R)*(B + R - 1)))*probs[R]
            p1 = 0
            if B > 1:
                p1 = B*(B - 1) / ((B + R)*(B + R - 1))
            new[R] = t / (1 - p1)
    return new

B = 12345
R = 24690
probs = [0]*(R + 1)
for b in range(1,B + 1):
    probs = next(probs,b,R)

print(round(probs[-1],10))

#Answer = 0.2928967987

#Time: 2:00