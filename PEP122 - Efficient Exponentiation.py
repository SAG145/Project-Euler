def power_compute(powers,n):
    power = []
    min1 = 200
    for k in range(1,n // 2 + 1):
        power1 = powers[k]
        power2 = powers[n - k]
        if max(minis[k],minis[n - k]) < min1:
            for p1 in power1:
                for p2 in power2:
                    p_new = tuple(sorted(dict.fromkeys(p1 + p2 + (n,))))
                    if len(p_new) < min1 + 1:
                        min1 = len(p_new)
                        power.append(p_new)
    power = list(dict.fromkeys(power))
    return power

powers = [[0],[(1,)],[(1,2)]]
minis = [0,0,1]
sum = 1
for k in range(3,201):
    p = power_compute(powers,k)
    min_len = 200
    for q in p:
        if len(q) < min_len:
            min_len = len(q)
    i = 0
    while i < len(p):
        if len(p[i]) > min_len:
            p.pop(i)
        else:
            i += 1
    minis.append(min_len - 1)
    sum += min_len - 1
    powers.append(p)
print(sum)

#Answer = 1582

