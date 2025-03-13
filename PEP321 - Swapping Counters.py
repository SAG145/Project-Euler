import math

def sol(sol1,sol2,n):
    a,b,c,d = sol1[0],sol1[1],sol2[0],sol2[1]
    return (a*c + b*d*n,a*d + b*c)

def square(n):
    if n < 0:
        return False
    return math.isqrt(n)**2 == n

final_sols = []
base_sols = [(3,1)]
for i in range(2,15*10**7):
    if square(-448 + 32*i**2):
        final_sols.append((math.isqrt(-448 + 32*i**2),i))
    if square(1 + 32*i**2):
        base_sols.append((math.isqrt(1 + 32*i**2),i))

for _ in range(10):
    new = []
    for s1 in final_sols:
        for s2 in base_sols:
            new.append(sol(s1,s2,8))
    final_sols = list(dict.fromkeys(new + final_sols))

final_sols.sort()
tri = []
num_of_sols = 0
for s in final_sols:
    y = -8 + math.isqrt(32*s[1]**2 - 448)
    if y % 16 == 0 and y > 0:
        y //= 16
        x = math.isqrt(16 + 8*y**2 + 8*y) - 4
        if x % 4 == 0:
            tri.append(x // 4)

print(sum(sorted(list(dict.fromkeys(tri)))[:40]))

#Answer = 2470433131948040
#Time: 2:00
