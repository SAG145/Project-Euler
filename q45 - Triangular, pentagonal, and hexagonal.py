tlist = []
plist = []
hlist = []
for n in range(1,100000):
    tlist.append((n**2-n)/2)
    plist.append((3*n**2-n)/2)
    hlist.append((2*n**2-n))
for i in tlist:
    if i in hlist:
        if i in plist:
            print(i)
#answer = 1533776805