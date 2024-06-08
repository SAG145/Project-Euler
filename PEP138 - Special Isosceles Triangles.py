import math
b_list = [16,272,4896]
l_list = [17,305,5473] #הקוד נכתב לאחר בדיקות רבות של התכונות שדרושות מ b בעזרת קוד יסודי
d_list = [18,323]
k = 2
j = 3
for i in range(9):
    if i % 2 == 0:
        b_list.append(b_list[-1] * l_list[-k] / l_list[-k - 1])
        l_list.append(math.sqrt((b_list[-1] / 2) ** 2 + (b_list[-1] + 1) ** 2))
        k += 1
    else:
        b_list.append(b_list[-1] * d_list[-1] / d_list[-2])
        l_list.append(math.sqrt((b_list[-1] / 2) ** 2 + (b_list[-1] - 1) ** 2))
        d_list.append(d_list[-1] + l_list[-j])
        j += 1

print(int(sum(l_list)))

#answer = 1118049290473932
