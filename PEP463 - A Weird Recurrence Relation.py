def smart_search_index(lst,elem,index = 0):
    if len(lst) == 0:
        return -1
    l = len(lst) // 2
    if lst[l][0] == elem:
        return index + l
    if lst[l][0] < elem:
        return smart_search_index(lst[l + 1:],elem,index + l + 1)
    else:
        return smart_search_index(lst[:l], elem, index)


def f(n,res_f):
    if n == 1 or n == 3:
        return n
    if n % 2 == 0:
        return f(n // 2,res_f)
    i = smart_search_index(res_f,n)
    if i != -1:
        return res_f[i][1]
    t = n // 4
    if n % 4 == 1:
        s = 2*f(2*t + 1,res_f) - f(t,res_f)
        res_f.append((n,s))
        res_f.sort()
        return s
    s = 3*f(2*t + 1,res_f) - 2*f(t,res_f)
    res_f.append((n,s))
    res_f.sort()
    return s

def S_odd(n,res_odd,res_f):
    i = smart_search_index(res_odd,n)
    if i != -1:
        return res_odd[i][1]
    if n == 1:
        return 1
    if n == 2:
        return 4
    if n % 2 == 1:
        s = f(2*n - 1,res_f) + S_odd(n - 1,res_odd,res_f)
        res_odd.append((n,s))
        res_odd.sort()
        return s
    s = 5*S_odd(n // 2,res_odd,res_f) - 3*S(n // 2 - 1,res,res_odd,res_f) - 1
    res_odd.append((n,s))
    res_odd.sort()
    return s

def S(n,res,res_odd,res_f):
    if n == 1:
        return 1
    i = smart_search_index(res,n)
    if i != -1:
        return res[i][1]
    s = S(n // 2,res,res_odd,res_f) + S_odd((n + 1) // 2,res_odd,res_f)
    res.append((n,s))
    res.sort()
    return s

res_odd = []
res = []
res_f = []

print(S(3**37,res,res_odd,res_f) % 10**9)

#Answer = 808981553