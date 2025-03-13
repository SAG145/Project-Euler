def rectangles(x,y):
    final_sum = 0
    for a in range(1,x+1):
        sum1 = 0
        for b in range(1,y+1):
            sum1 += (x-a+1)*(y-b+1)
        final_sum += sum1
    return final_sum

nearest_solution = 100000
area = 0
for x in range(1,100):
    for y in range(1,x):
        rectangle = rectangles(x,y)
        if abs(rectangle-2000000) < nearest_solution:
            nearest_solution = abs(rectangle-2000000)
            area = x*y
print(area)

#Answer = 2772

