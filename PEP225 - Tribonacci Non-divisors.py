def tribonacci(n,index,list1):
    if n < index + 1:
        return list1[n]
    else:
        return tribonacci(n - 1,index,list1) + tribonacci(n - 2,index,list1) + tribonacci(n - 3,index,list1)

index = 3
list1 = [0,1,1,1]
for k in range(index + 1,100000):
    list1.append(tribonacci(k,index,list1))
    index += 1

list1.pop(0)
odd = []
i = 1
while len(odd) < 124:
    divide = False
    for k in list1:
        if k % i == 0:
            divide = True
            break
    if not divide:
        odd.append(i)
    i += 2
print(odd[-1])

#Answer = 2009

