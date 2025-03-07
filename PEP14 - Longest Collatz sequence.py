def collatz(n):
    i = 1
    while n!=1:
        if n%2==0:
            n = n/2
        else:
            n = n*3+1
        i += 1
    return i
    
y = 0
x = 0
for i in range(1,1000000):
    k = collatz(i)
    if k>y:
        y = k
        x = i
print(x)

#answer = 837799
