import math

def F(x):
    return math.floor(2 ** (30.403243784 - x ** 2)) * 10 ** -9

def u(n,values_list,index_list):
    if n == 0:
        return -1
    elif index_list[-1] > n-1:
        return values_list[n]
    else:
        return F(u(n-1,values_list,index_list))

index_list = []
values_list = []
for k in range(100002):
    x = u(k,values_list,index_list)
    index_list.append(k)
    values_list.append(x)
print(u(10**5,values_list,index_list)+u(10**5+1,values_list,index_list))

#Answer = 1.710637717

