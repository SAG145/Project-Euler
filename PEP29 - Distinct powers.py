lst = []
for i in range(2,101):
    for k in range(2,101):
        n = i**k
        if n in lst:
            print("n = ",n,k,i)
        else:
            lst.append(n)
print(len(lst))

#Answer = 9183

