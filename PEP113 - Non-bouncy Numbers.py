def next(lst):
    new = [0]*10
    for i in range(10):
        for j in range(i,10):
            new[i] += lst[-1][j]
    lst.append(new)

def dec(n):
    for i in range(1,len(lst)):
        if int(n[i])  >int(n[i - 1]):
            return False
    return True

lst = [[0] + [1]*9]
for i in range(99):
    next(lst)

s = 0
for t in lst:
    s += sum(t) + sum(t[1:])

print(s - 9*100)

#answer = 51161058134250
#This code was written after solving the problem because it was unclear why the original code worked
