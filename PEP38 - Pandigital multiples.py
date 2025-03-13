def double(str1):
    lst = []
    a = False
    for i in str1:
        if i in lst:
            a = True
            break
        else:
            lst.append(i)
    return a

x = - 1
for i in range(25,34):
    h = str(i) + str(2*i) + str(3*i) + str(4*i)
    if double(h) == False and (("0" in h) == False):
        if int(h) > x:
            x = int(h)

for k in range(100,334):
    s = str(k) + str(2*k) + str(3*k)
    if double(s) == False and (("0" in s) == False):
        if int(s) > x:
            x = int(s)

for m in range(5000,10000):
    v = str(m) + str(2*m)
    if double(v) == False and (("0" in v) == False):
        if int(v) > x:
            x = int(v)
print(x)

#Answer = 932718654

