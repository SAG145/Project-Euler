a = 1504170715041707
b = 4503599627370517
euler_coin = 10**25
sum = 0
last_k = 1
k = 1
while euler_coin > 0: #האלגוריתם נוצר לאחר הבנה של ה k'ים שנותנים eulercoin חדש בדרך יסודית
    l = 2
    while True:
        if (a*(k*l-last_k)) % b < euler_coin:
            k1 = k
            euler_coin = (a*(k*l-last_k)) % b
            sum += euler_coin
            k = k*l - last_k
            last_k = k1
            break
        else:
            l += 1
print(sum)

#answer = 1517926517777556