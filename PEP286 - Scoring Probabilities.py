def chance(q):
    lst = [1] + [0]*20
    for x in range(1,51):
        new = [0]*21
        new[0] = lst[0]*(x / q)
        for p in range(1,21):
            new[p] = lst[p]*(x / q) + lst[p - 1]*(1 - x / q)
        lst = new
    return lst[20]

l = 50
r = 100
for _ in range(100):
    q = (l + r) / 2
    if chance(q) > 0.02:
        l = q
    else:
        r = q

print(round(q,10))

#Answer = 52.6494571953