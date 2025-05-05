def max_power_divides(n,p):
    power = 0
    while n % p == 0:
        n //= p
        power += 1
    return power

def max_elem(lst):
    for i in range(len(lst) - 1,-1,-1):
        if lst[i] != 0:
            return i

def S(u,k):
    dlist = [1]*(u + 1)
    for i in range(2,len(dlist)):
        if dlist[i] == 1:
            for j in range(i,len(dlist),i):
                dlist[j] *= max_power_divides(j,i) + 1

    curr_d = [0]*(max(dlist) + 1)
    for i in range(1,k + 1):
        curr_d[dlist[i]] += 1

    maxi = max_elem(curr_d)
    s = maxi
    for n in range(2,u - k + 2):
        curr_d[dlist[n - 1]] -= 1
        curr_d[dlist[n + k - 1]] += 1
        if dlist[n + k - 1] > maxi:
            maxi = dlist[n + k - 1]
        if dlist[n - 1] == maxi and curr_d[dlist[n - 1]] == 0:
            maxi = max_elem(curr_d)
        s += maxi
    return s

print(S(100000000,100000))

#Answer = 51281274340

#Time: 3:30