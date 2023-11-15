x = 0
for i in range(1,1000):
    x1 = (i//100)
    x2 = (i-x1*100)//10
    x3 = i%10
    twe_or_eve = False
    if x1 == 1 or x1 == 2 or x1 == 6:
        x += 10
    elif x1 == 4 or x1 == 5 or x1 == 9:
        x += 11
    elif x1 ==0:
        None
    else:
        x += 12

    if x3 == 1 or x3 == 2:
        if x2 == 1:
            x += 6
            twe_or_eve = True
        else:
            x += 3
    if x2 == 1:
        None
    else:
        if x3 == 6:
            x += 3
        elif x3 == 4 or x3 == 5 or x3 == 9:
            x += 4
        elif x3 == 0:
            None
        elif x3 == 3 or x3 == 7 or x3 == 8:
            x += 5

    if x2 == 1:
        if twe_or_eve:
            None
        elif x3 == 0:
            x += 3
        elif x3 == 3 or x3 == 4 or x3 == 8 or x3 == 9:
            x += 8
        elif x3 == 5 or x3 == 6:
            x += 7
        else:
            x += 9
    elif x2 == 2 or x2 == 3 or x2 == 8 or x2 == 9:
        x += 6
    elif x2 == 4 or x2 == 5 or x2 == 6:
        x += 5
    elif x2 == 0:
        None
    else:
        x += 7

    if x1>0:
        if x2 == 0 and x3 == 0:
            None
        else:
            x += 3
print(x+11)
#answer = 21124