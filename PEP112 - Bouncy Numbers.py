def bouncy(n):
    s = str(n)
    len1 = len(s)
    decreasing,increasing = True,True
    for d1 in range(len1 - 1):
        if s[d1] < s[d1+1]:
            decreasing = False
    for d2 in range(len1-1):
        if s[d2] > s[d2+1]:
            increasing = False
    return not (increasing or decreasing)

num = 100
bouncy_count = 0
while True:
    if bouncy(num):
        bouncy_count += 1
    if bouncy_count / num == 0.99:
        print(num)
        break
    num += 1

#Answer = 1587000

