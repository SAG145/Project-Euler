y = 0
for i in range(101,1000):
    for j in range(101,1000):
        x = str(i*j)
        if x==x[::-1] and i*j>y:
            y = i*j
print(y)

#answer = 906609