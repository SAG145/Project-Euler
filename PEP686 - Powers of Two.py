def next_a(a: object, p2: object) -> object:
    return str(a*p2)[:4000]

a = 2**90
j = 90
c123 = 1
m = [2**196,2**289,2**485]
while c123 < 678910:
    na = next_a(a,m[0])
    found = False
    if na[:3] == "123":
        found = True
        a = int(na)
        c123 += 1
        j += 196
    na = next_a(a,m[1])
    if not found and na[:3] == "123":
        found = True
        a = int(na)
        c123 += 1
        j += 289
    na = next_a(a,m[2])
    if not found and na[:3] == "123":
        found = True
        a = int(na)
        c123 += 1
        j += 485

print(j)

#Answer = 193060223

#Time: 13:00
