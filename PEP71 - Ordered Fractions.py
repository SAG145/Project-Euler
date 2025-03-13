import math

min_dis = 1
num = 0
for d in range(1,10**6 + 1):
    a = math.floor(3*d / 7)
    b = math.ceil(3*d / 7)
    dis = 3 / 7 - a / d
    if dis > 0 and dis < min_dis:
        min_dis = dis
        num = a
    if a != b:
        dis = 3 / 7 - b / d
        if dis > 0 and dis < min_dis:
            min_dis = dis
            num = b

print(num)

#Answer = 428570

#This code was written after solving the problem because the original code for solving the problem was lost.
