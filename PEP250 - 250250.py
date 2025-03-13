import copy

def next_num(n,mods_sums,mod):
    new = copy.copy(mods_sums)
    for m in range(250):
        new[(m + n) % 250] = (new[(m + n) % 250] + mods_sums[m]) % mod
    return new

mod = 10**16
mods = []
for a in range(1,250251):
    mods.append(pow(a,a,250))
mods_sums = [1] + [0]*249
i = 1
for k in mods:
    mods_sums = next_num(k,mods_sums,mod)
    i += 1

print(mods_sums[0] - 1)

#Answer = 1425480602091519

