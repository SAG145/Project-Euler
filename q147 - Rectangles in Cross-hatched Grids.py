def straight_rectangles(x,y):
    final_sum = 0
    for a in range(1,x+1):
        sum1 = 0
        for b in range(1,y+1):
            sum1 += (x-a+1)*(y-b+1)
        final_sum += sum1
    return final_sum

def minimum(x,y):
    if x % 2 == y % 2:
        if x % 2 == 0:
            return (((x+y)//2,(x+y)//2),1)
        else:
            return (((x+y)//2,(x+y)//2 + 1),1)
    else:
        if x == 1:
            return  

# def diagonal_rectangles(x,y):
#     if x == 1:
#         return y - 1
#     else:
#
def smaller(x,y):
    sum = 0
    for k in range(x + 1, y + 1):
        sum += diagonal_rectangles(x,x + k)
    for x in range(1,x + 1):
        for y in range(1,x + 1):
            sum += diagonal_rectangles(x,y)
    return sum

# print(smaller(43,47))

print(straight_rectangles(4,3))