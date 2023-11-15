import math
perimeters_sum = 16 #הקוד נכתב על בסיס תצפיות אמפיריות על תוצאות בבדיקה יסודית
ratio_list = [3,8,33]
for k in range(20):
    if k % 2 == 0:
        ratio_list.append(4*ratio_list[-1] -4 - ratio_list[-2])
    else:
        ratio_list.append(4 * ratio_list[-1] + 4 - ratio_list[-2])
x = 6
for r in range(len(ratio_list)-1):
    if x < 10**9//3//3.71 + 2:
        x *= ratio_list[r + 1] / ratio_list[r]
        if r % 2 == 0:
            perimeters_sum += 3*x + 2
        else:
            perimeters_sum += 3*x - 2
    else:
        break
print(int(perimeters_sum))

#answer = 518408346