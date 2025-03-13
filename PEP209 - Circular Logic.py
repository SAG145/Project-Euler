def XOR(x,y):
    if x == y:
        return 0
    return 1

def AND(x,y):
    return x == 1 and y == 1

def func(bits):
    new_bits = bits[1:] + (XOR(bits[0],AND(bits[1],bits[2])),)
    return new_bits

inputs = []
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    for f in range(2):
                        inputs.append((a,b,c,d,e,f))

groups = []
i = 0
while len(inputs) > 0:
    lst = [inputs[0]]
    k = func(inputs[0])
    inputs.pop(0)
    while k not in lst:
        lst.append(k)
        inputs.remove(k)
        k = func(k)
    groups.append(lst)
f = [1,1]
for i in range(2,65):
    f.append(f[-1] + f[-2])

s = 1
for g in groups:
    if len(g) != 1:
        l = len(g)
        s *= (f[l] + f[l - 2])
print(s)

#Answer = 15964587728784

