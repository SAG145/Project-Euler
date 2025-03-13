pita_triplet = []

def sumone(tuple):
    sum = 0
    for a in tuple:
        sum += a
    return sum

for m in range(2,1225):
    for n in range(1,m):
        sum = 2*m**2 + 2*m*n
        a = m**2 + n**2
        b = 2*m*n
        c = m**2 - n**2
        if b < c:
            d = c
            c = b
            b = d
        for k in range(1,1500001 // sum + 2):
            pita_triplet.append((a*k,b*k,c*k))

pita_triplet = list(dict.fromkeys(pita_triplet))
l_list = [0]*1500001
for t in pita_triplet:
    s = sumone(t)
    if s < 1500001:
        l_list[s] += 1

single = 0
for l in l_list:
    if l == 1:
        single += 1
print(single)

#Answer = 161667

