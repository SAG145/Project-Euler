import copy
list1 = [1]*10
sum1 = 0
for k in range(99):
    lst = copy.copy(list1)
    for d in range(10):
        lst[d] = sum(list1[:d + 1])
    list1 = copy.copy(lst)
    sum1 += sum(list1)
print(sum1 + sum(list1) - 10*100 + 9)

#answer = 51161058134250
#לא ברור למה הקוד עובד