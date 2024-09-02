import math

def straight_rectangles(x,y):
    final_sum = 0
    for a in range(1,x+1):
        sum1 = 0
        for b in range(1,y+1):
            sum1 += (x-a+1)*(y-b+1)
        final_sum += sum1
    return final_sum

def minimum(x,y):
    a = math.ceil(x / 2)
    b = (math.ceil(y / 2))
    return (a + b,math.ceil(x / 2 + y / 2))

def contains(a,b,x,y):
    rectangles = 0
    back_even = math.ceil(y / 2)
    forward_even = math.ceil(x / 2)
    up_even = math.ceil(x / 2 + y / 2)
    rec_even = a - back_even - forward_even + 1
    rectangles += rec_even*(b - up_even + 1)

    back_odd = math.ceil(y / 2 - 1 / 2)
    forward_odd = math.ceil(x / 2 - 1 / 2)
    up_odd = math.ceil(x / 2 + y / 2 + 1 / 2)
    rec_odd = a - back_odd - forward_odd
    rectangles += rec_odd * (b - up_odd + 1)
    if x == y:
        return rectangles
    return rectangles*2

def rectangles(a,b):
    rec = straight_rectangles(a,b)
    x = 1
    maxi = False
    while True:
        y = 1
        while y <= x:
            r = contains(a,b,x,y)
            if r == 0:
                break
            rec += r
            y += 1
        if y == 1:
            return rec
        x += 1

rec_sit = 0
for a in range(1,48):
    for b in range(1,44):
        recs = rectangles(a,b)
        rec_sit += recs

print(rec_sit)

#answer = 846910284