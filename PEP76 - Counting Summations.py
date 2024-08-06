def partitions_to_k_parts(n,k,partitions_list):
    if n == 0 and k == 0:
        return 1
    elif n < 1 or k < 1:
        return 0
    elif k < index_list[n][-1] + 1:
        return partitions_list[n][k]
    else:
        return partitions_to_k_parts(n-k,k,partitions_list) + partitions_to_k_parts(n-1,k-1,partitions_list)

def parititions(n):
    sum = 0
    for k in range(n):
        # print(k)
        sum += partitions_to_k_parts(n,k,partitions_list)
    return sum

partitions_list = []
index_list = []
for k in range(101):
    partitions_list.append([])
    index_list.append([])

for i in range(101):
    for j in range(101):
        partitions_list[i].append(partitions_to_k_parts(i,j,partitions_list))
        index_list[i].append(j)
print(parititions(100))

#answer = 190569291
