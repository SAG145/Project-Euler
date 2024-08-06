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
#  יוצא 30952867 ו 60357289 אבל צריך גם להכניס את 06357289 ואז פשוט משלימים 1 או 4 כי אלה שתי הספרות שלא משתתפות

# print(1430952867 + 4130952867 + 1460357289 + 4160357289 + 1406357289 + 4106357289) = 16695334890

#answer = 16695334890
