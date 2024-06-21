import math
fib = [1,1]
while fib[-1] < 1000001:
    fib.append(fib[-1] + fib[-2])
fib.pop(-1)
fib.pop(0)

steps = []
for f in fib:
    for k in range(f):
        a = f**2 - k**2
        sqrt1 = math.isqrt(a)
        if math.isqrt(a)**2 == a and k < 10001 and sqrt1 < 10001:
            steps.append((sqrt1,k))
            steps.append((k,sqrt1))
steps = list(dict.fromkeys(steps))
steps.sort()

print(steps)
print(len(steps))

def new_path(paths,steps,mod,x,y):
    path = 0
    for step in steps:
        if step[0] <= x and step[1] <= y:
            path += paths[x - step[0]][y - step[1]]
    path = path % mod
    paths[x][y] = path
    paths[y][x] = path

mod = 10**9 + 7
paths = []
for i in range(10001):
    paths.append([0]*10001)

paths[0][0] = 1
for y in range(10**4 + 1):
    print(y)
    for x in range(y + 1):
        if x != 0 or y != 0:
            new_path(paths,steps,mod,x,y)
new_path(paths,steps,mod,0,1)

print(paths[10000][10000])

#זמן הרצה - 17 דקות