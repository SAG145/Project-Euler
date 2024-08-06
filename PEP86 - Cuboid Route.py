import math
def int_mini_path(a,b,c):
    min_path = min(a**2 + (b + c)**2,b**2 + (a + c)**2,c**2 + (a + b)**2)
    return perfect_square(min_path)

def perfect_square(n):
    return math.floor(math.sqrt(n))**2 == n

x = 0
M = 100000
for a in range(1,M + 1):
    if x > 1000000:
        print(a - 1)
        break
    for b in range(1,a + 1):
        for c in range(1, b + 1):
            if int_mini_path(a,b,c):
                x += 1

#answer = 1818
#זמן הרצה: בערך רבע שעה
