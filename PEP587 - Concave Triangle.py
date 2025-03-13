import math

def area_under_the_circle(x):
    a = math.sqrt(-(x - 2)*x)
    return (-x*(a - 2) + a + 2*math.asin(math.sqrt(1 - x/2))) / 2

def area(x):
    return area_under_the_circle(x) - area_under_the_circle(0)

def ratio(n):
    x_inter = (-math.sqrt(2)*n**(3/2) + n**2 + n) / (n**2 + 1)
    y_inter = x_inter / n
    s = x_inter*y_inter/2 + area(1) - area(x_inter)
    return s / area(1)

n = 1
while ratio(n) > 0.001:
    n += 1
print(n)

#Answer = 2240

