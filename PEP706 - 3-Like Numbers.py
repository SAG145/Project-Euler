def dec_to_base3(dec):
    ter = []
    p = 1
    while p*3 <= dec:
        p *= 3
    while p > 0:
        d = dec // p
        ter.append(d)
        dec -= p*d
        p //= 3
    return [0]*(6 - len(ter)) + ter

def base3_to_dec(ter):
    dec = 0
    ter = ter[::-1]
    for i in range(len(ter)):
        dec += ter[i]*3**i
    return dec

def targets(ters,i):
    tars = []
    for dig in range(3):
        t2 = [0]*3
        t2[dig] = 1
        for j in range(3,6):
            t2[(j + dig) % 3] = (t2[(j + dig) % 3] + ters[i][j]) % 3
        t1 = [0]*3
        for k in range(3):
            t1[k] = (t2[k] + ters[i][k]) % 3
        tars.append(base3_to_dec(t1 + t2))
    return tars

mod = 10**9 + 7
ters = []
for n in range(729):
    ters.append(dec_to_base3(n))

all_targets = []
for i in range(729):
    all_targets.append(targets(ters,i))

poss = [0]*729
poss[1 + 27] = 3
poss[3 + 81] = 3
poss[9 + 243] = 3
for _ in range(10**5 - 1):
    new = [0]*729
    for i in range(729):
        for j in range(3):
            if j == 0:
                new[all_targets[i][j]] = (new[all_targets[i][j]] + 4*poss[i]) % mod
            else:
                new[all_targets[i][j]] = (new[all_targets[i][j]] + 3*poss[i]) % mod
    poss = new

s = 0
for i in range(729):
    if dec_to_base3(i)[0] == 0:
        s += poss[i]
print(s % mod)

#answer = 884837055

#Time: 1:30