ways = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                s = a + b + c + d
                for e in range(min(10,s + 1)):
                    for f in range(min(10,s - e + 1)):
                        for g in range(min(10,s - e - f + 1)):
                            for j in range(min(10,s - b - f + 1,s - d - g + 1)):
                                for p in range(min(10,s - a - f + 1,s - d + 1)):
                                    h = s - e - f - g
                                    l = s - d - h - p
                                    m = s - j - g - d
                                    i = s - a - e - m
                                    k = s - i - j - l
                                    n = s - b - f - j
                                    o = s - c - g - k
                                    if a + f + k + p == s and m + n + o + p == s:
                                        if min(h,l,m,i,k,n,o) >= 0 and max(h,l,m,i,k,n,o) < 10:
                                            ways += 1

print(ways)

#Answer = 7130034
#Time: 8:00

