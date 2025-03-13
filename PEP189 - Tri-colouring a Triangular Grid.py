import math
import copy

def max_log3(n):
    a = 0
    while 3**a < n + 1:
        a += 1
    return a - 1

def ter(n):
    pre_power = max_log3(n)
    num = str(n // 3**pre_power)
    n -= (n // 3**pre_power)*3**pre_power
    while n > 0:
        power = max_log3(n)
        num += "0"*(pre_power - power - 1) + str(n // 3**power)
        n -= (n // 3**power)*3**power
        pre_power = power

    num += "0"*(pre_power)
    return num

ter_list = ["0"]
for n in range(1,3**8):
    ter_list.append(ter(n))

def ter_len(n,len1):
    num = ter_list[n]
    num = "0"*(len1 - len(num)) + num
    return num

def valid_same_line(num1,num2):
    if num1[0] == num2[0] or num1[-1] == num2[-1]:
        return False
    for d in range(1,len(num2) - 1):
        if num2[d] == num1[d] or num2[d] == num1[d - 1]:
            return False
    return True

def valid_next_line(num1,num2):
    for d in range(len(num1)):
        if num1[d] == num2[d]:
            return False
    return True

valid_same_line_by_len = [[]]
valid_next_line_by_len = [[]]
for len1 in range(1,8):
    sll = []
    for n in range(3**len1):
        vn = []
        num1 = ter_len(n,len1)
        for m in range(3**(len1 + 1)):
            if valid_same_line(num1,ter_len(m,len1 + 1)):
                vn.append(m)
        sll.append(vn)
    valid_same_line_by_len.append(sll)

for len2 in range(1,8):
    sll = []
    for n in range(3**len2):
        vn = []
        num1 = ter_len(n,len2)
        for m in range(3**len2):
            if valid_next_line(num1,ter_len(m,len2)):
                vn.append(m)
        sll.append(vn)
    valid_next_line_by_len.append(sll)

confi = [1,1,1] + [0]*(3**8 - 3)
for k in range(1,15):
    if k % 2 == 1:
        new_confi = [0]*3**8
        for i in range(len(confi)):
            if confi[i] != 0:
                for n in valid_next_line_by_len[(k - 1) // 2 + 1][i]:
                    new_confi[n] += confi[i]
        confi = copy.copy(new_confi)
    else:
        new_confi = [0]*3**8
        for i in range(len(confi)):
            if confi[i] != 0:
                for n in valid_same_line_by_len[(k - 1) // 2 + 1][i]:
                    new_confi[n] += confi[i]
        confi = copy.copy(new_confi)
print(sum(confi))

#Answer = 10834893628237824

