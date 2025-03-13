def u(n):
    s = 0
    for d in range(11):
        s += (-n)**d
    return s

values = []
sum1 = 0
for k in range(1,11):
    values.append(u(k))

for i in range(1,11):
    lst = values[:i]
    poli = [lst]
    while len(poli[-1]) != 1:
        list1 = []
        for m in range(1,len(poli[-1])):
            list1.append(poli[-1][m] - poli[-1][m - 1])
        poli.append(list1)
    for j in range(2,len(poli) + 1):
        poli[-j].append(poli[-j + 1][-1] + poli[-j][-1])
    sum1 += poli[0][-1]
print(sum1)

#Answer = 37076114526

