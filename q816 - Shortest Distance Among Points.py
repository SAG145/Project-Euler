import math
def distance(p1,p2):
    d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    return d

def d(k):
    points1 = []
    x_list = []
    y_list = []
    s = 290797
    for n in range(k):
        x = s
        y = (x**2) % 50515093
        s = (y**2) % 50515093
        points1.append((x,y))
        x_list.append(x)
        y_list.append(y)
    points1.sort()
    min_distance = math.inf
    for i in range(k-5):
        d1 = min(distance(points1[i],points1[i+1]),distance(points1[i],points1[i+2]),distance(points1[i],points1[i+3]),distance(points1[i],points1[i+4]),distance(points1[i],points1[i+5]))
        if d1 < min_distance:
            min_distance = d1
    return round(min_distance*10**9)/10**9

print(d(2000000))

#answer = 20.880613018