from math import comb

def num_of_wins_sim(l):
    m = min(499, l)
    s = 0
    lst = [0] * (m + 1)
    for i in range(m, 0, -1):
        a = comb(499,i)*2**i*i**l
        d = 1 - lst[i]
        s += a*d
        for j in range(1,i):
            lst[j] += d*comb(499 - j, i - j)*2**(i - j)
    return 998**l - s

lst_nws = []
for i in range(250):
    lst_nws.append(num_of_wins_sim(i))
lst_nws[0] = 0

num_of_wins = 0
e = 0
for n in range(2,250):
    new = 0
    for n0 in range(n + 1):
        for n500 in range(n - n0 + 1):
            t = comb(n,n0)*comb(n - n0,n500)
            if n500 > 1:
                new += t*998**(n - n0 - n500)
            else:
                new += t*lst_nws[n - n0 - n500]
    e += n*(new - 1000*num_of_wins) / 1000**n
    num_of_wins = new

print(round(e,8))

#Answer = 40.66368097