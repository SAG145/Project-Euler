x = 0
for i in range(1,100):
    for k in range(1,100):
        if len(str(i**k)) == k:
            x += 1
print(x)
#answer = 49