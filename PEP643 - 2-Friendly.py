import math

def smart_search_in_sorted_list(k,lst):
    l = len(lst) // 2
    if len(lst) == 0:
        return False
    if lst[0][0] == k:
        return True
    elif l == 0:
        return False
    elif lst[l][0] > k:
        return smart_search_in_sorted_list(k,lst[:l])
    else:
        return smart_search_in_sorted_list(k,lst[l:])

def tot_summ(n,ts_list,ts_list2):
    if n < len(ts_list) and ts_list[n] != -1:
        return ts_list[n]
    if smart_search_in_sorted_list(n,ts_list2):
        for ts2 in ts_list2:
            if ts2[0] == n:
                return ts2[1]
    ts = n*(n - 1) // 2
    for i in range(1,math.isqrt(n) + 1):
        if i > 1:
            ts -= tot_summ(n // i,ts_list,ts_list2)
        if i != n // i:
            ts -= (n // i - n // (i + 1))*tot_summ(i,ts_list,ts_list2)
    if n > 10**7:
        ts_list2.append((n,ts))
        ts_list2.sort()
    if n < 10**7:
        ts_list[n] = ts
    return ts

def f(n):
    ts_list = [-1]*(10**7)
    ts_list[2] = 1
    ts_list2 = []
    for i in range(3,math.isqrt(n) + 3):
        tot_summ(i,ts_list,ts_list2)
    p2 = 2**math.floor(math.log(n,2))
    pairs = 0
    while p2 > 1:
        ts2 = tot_summ(n // p2,ts_list,ts_list2)
        pairs += ts2
        p2 //= 2
    return pairs

print(f(10**11) % (10**9 + 7))

#Answer = 968274154

#Time: 3:00