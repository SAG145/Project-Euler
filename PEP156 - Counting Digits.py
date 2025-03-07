def f(n,d):
    s = str(n)
    l = len(s)
    x = 0
    d1 = int(s[0])
    if d1 > d:
        x += 10**(l - 1)
    elif d1 == d:
        x += int(s[1:]) + 1

    for i in range(1,len(s)):
        e = int(s[i])
        if e > d:
            x += (int(s[:i]) + 1)*10**(l - i - 1)
        elif e == d:
            x += 1
            x += (int(s[:i]))*10**(l - i - 1)
            if i != l - 1:
                x += int(s[i + 1:])
        else:
            x += (int(s[:i]))*10**(l - i - 1)
    return x

def s(d):
    solutions_sum = 0

    pre = 10
    for k in range(2*10**4,10**11,10**4):
        f1 = f(k,d)
        if pre*(f1 - k) <= 0:
            for l in range(k - 10**4,k):
                if f(l,d) == l:
                    solutions_sum += l
                    print(l,d,solutions_sum)
        pre = f1 - k

    return solutions_sum

x = 22786974071
for d in range(2,10):
    x += s(d)

print(x)

#answer = 21295121502550
#7 minutes and 30 seconds
