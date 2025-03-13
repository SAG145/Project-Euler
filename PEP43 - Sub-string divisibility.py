def double(str1):
    a = False
    lst = []
    for i in str1:
        if i in lst:
            a = True
            break
        else:
            lst.append(i)
    return a

for i in range(10000000,100000000):
    k = str(i)
    if double(k) == False:
        if int(k[5:]) % 17 == 0:
            if int(k[4:7]) % 13 == 0:
                if int(k[3:6]) % 11 == 0:
                    if int(k[2:5]) % 7 == 0:
                        if int(k[1:4]) % 5 == 0:
                            if int(k[:3]) % 3 == 0:
                                if int(k[1]) % 2 == 0:
                                    print(k)

# Comes out 30952867 and 60357289, but you also need to enter 06357289 and then simply add 1 or 4 because those are the two digits that don't participate.

print(1430952867 + 4130952867 + 1460357289 + 4160357289 + 1406357289 + 4106357289)

#Answer = 16695334890
