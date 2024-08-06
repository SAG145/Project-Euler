import math
target = 10**16
s = 2*math.floor(math.sqrt(target))
limit = math.floor(2*math.sqrt(target) / math.sqrt(163))
for y in range(1,limit + 1):
    d = -163*y**2 + 4*target
    delta = math.sqrt(d)
    x1 = (delta - y) // 2
    x2 = (-delta - y) // 2
    num_of_x = x1 - x2
    s += int(2*num_of_x)

print(s)

#answer = 4921370551019052
