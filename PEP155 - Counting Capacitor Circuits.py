import fractions
import copy

def partitions(n):
    if n == 1:
        return [[1]]
    p = partitions(n - 1)
    part = []
    for par in p:
        for k in range(len(par)):
            par1 = copy.copy(par)
            par1[k] += 1
            part.append(sorted(par1))
        part.append([1] + par)
    return remove_dup(sorted(part))

def remove_dup(list):
    i = 0
    while i < len(list) - 1:
        if list[i] == list[i + 1]:
            list.pop(i)
        else:
            i += 1
    return list

def parallel(lst):
    return sum(lst)

def series(lst):
    s = 0
    for f in lst:
        s += 1 / f
    return 1 / s

def new_values(values,part,caps,capacitors,i):
    if i == len(part):
        values.append(parallel(caps))
        values.append(series(caps))
    else:
        for c in capacitors[part[i]]:
            new_values(values,part,caps + [c],capacitors,i + 1)

def new_capa(n,capacitors):
    values = []
    a = 0
    parti = partitions(n)
    for p in parti:
        a += 1
        if p != [n]:
            new_values(values,p,[],capacitors,0)
    return list(dict.fromkeys(values))

capacitors = [[],[fractions.Fraction(60)]]
for c in range(2,19):
    capacitors.append(new_capa(c,capacitors))

all_capa = []
for c in capacitors:
    all_capa += c

print(len(list(dict.fromkeys(all_capa))))

#Answer = 3857447
#Time: 11:30
