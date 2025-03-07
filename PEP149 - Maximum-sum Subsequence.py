import copy

from time import perf_counter
start = perf_counter()
def sum_indexes(lst,start,end):
    s = 0
    for i in range(start,end + 1):
        s += lst[i]
    return s

def smart_search_index(lst,elem,index = 0):
    if len(lst) == 0:
        return -1
    l = len(lst) // 2
    if lst[l] == elem:
        return index + l
    if lst[l] < elem:
        return smart_search_index(lst[l + 1:],elem,index + l + 1)
    else:
        return smart_search_index(lst[:l], elem, index)

def max_sum_sub(lst,checkpoints):
    max_sum = 0
    starts = copy.copy(checkpoints)
    i = 0
    si = 0
    sj = 0
    while i < len(starts):
        s = lst[starts[i]]
        for j in range(smart_search_index(checkpoints,starts[i]) + 1,len(checkpoints)):
            s += sum_indexes(lst,checkpoints[j - 1] + 1,checkpoints[j])
            if s > max_sum:
                max_sum = s
                si = starts[i]
                sj = checkpoints[j]
            if s - lst[checkpoints[j]] > 0 and smart_search_index(starts,checkpoints[j]) != -1:
                starts.remove(checkpoints[j])
        i += 1
    return max_sum

verticals = []
horizontals = []
for i in range(2000):
    verticals.append(([],[]))
    horizontals.append(([],[]))
LFG = []
for k in range(1,56):
    sk = (100003 - 200003*k + 300007*k**3) % 1000000 - 500000
    LFG.append(sk)
    verticals[k - 1][0].append(sk)
    horizontals[0][0].append(sk)
    if sk > 0:
        verticals[k - 1][1].append(0)
        horizontals[0][1].append(k - 1)
for k in range(55,4*10**6):
    sk = (LFG[k - 24] + LFG[k - 55] + 1000000) % 1000000 - 500000
    LFG.append(sk)
    verticals[(k - 1) % 2000][0].append(sk)
    horizontals[(k - 1) // 2000][0].append(sk)
    if sk > 0:
        verticals[(k - 1) % 2000][1].append((k - 1) // 2000)
        horizontals[(k - 1) // 2000][1].append((k - 1) % 2000 - 1)

diagonals = []
for k in range(1999):
    diag = []
    checks = []
    j = k
    i = 0
    last = False
    while j // 2000 < 2000 and not (last and j % 2000 == 0):
        diag.append(LFG[j])
        if diag[-1] > 0:
            checks.append(i)
        i += 1
        j += 2001
        if j % 2000 == 1999:
            last = True
    di = copy.copy(diag)
    ch = copy.copy(checks)
    diagonals.append((di,ch))

for k in range(2000,4*10**6 - 4000 + 1,2000):
    diag = []
    checks = []
    j = k
    i = 0
    last = False
    while j // 2000 < 2000 and not (last and j % 2000 == 0):
        diag.append(LFG[j])
        if diag[-1] > 0:
            checks.append(i)
        i += 1
        j += 2001
        if j % 2000 == 1999:
            last = True
    di = copy.copy(diag)
    ch = copy.copy(checks)
    diagonals.append((di, ch))

for k in range(1,2000):
    diag = []
    checks = []
    j = k
    i = 0
    last = False
    while j // 2000 < 2000 and not (last and j % 2000 == 1):
        diag.append(LFG[j])
        if diag[-1] > 0:
            checks.append(i)
        i += 1
        j += 1999
        if j % 2000 == 0:
            last = True
    di = copy.copy(diag)
    ch = copy.copy(checks)
    diagonals.append((di, ch))

for k in range(3999, 4*10**6 - 1,2000):
    diag = []
    checks = []
    j = k
    i = 0
    last = False
    while j // 2000 < 2000 and not (last and j % 2000 == 1):
        diag.append(LFG[j])
        if diag[-1] > 0:
            checks.append(i)
        i += 1
        j += 1999
        if j % 2000 == 0:
            last = True
    di = copy.copy(diag)
    ch = copy.copy(checks)
    diagonals.append((di, ch))

max_sum = 0
a = 0
for v in verticals:
    a += 1
    ns = max_sum_sub(v[0],v[1])
    if ns > max_sum:
        max_sum = ns

for h in horizontals:
    a += 1
    ns = max_sum_sub(h[0],h[1])
    if ns > max_sum:
        max_sum = ns

for d in diagonals:
    a += 1
    ns = max_sum_sub(d[0],d[1])
    if ns > max_sum:
        max_sum = ns
print(max_sum)

#answer = 52852124
#6 minutes
