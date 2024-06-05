import math
def solution(c):
    a = (8 + 4*c) // 16
    return (a,int((1 + math.sqrt(8*a**2 + 8*a + 1)) / 2))

def next(t):
    n = t[0]
    m = t[1]
    return (3*n + 4*m,3*m + 2*n)

t = (2,1)
while solution(t[0])[1] < 10**12 + 1:
    t = next(t)
print(solution(t[0])[0])

#answer = 756872327473
