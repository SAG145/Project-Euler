stealthys = []
limit = 10**14
i = 1
while 2*i*(i + 1) <= limit:
    a = i*(i + 1)
    j = 1
    while j <= i and j*(j + 1)*a <= limit:
        stealthys.append(j*(j + 1)*a)
        j += 1
    i += 1

print(len(list(dict.fromkeys(stealthys))))

#answer = 75737353
#3 minutes and 30 seconds