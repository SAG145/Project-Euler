import math

def palindromic(n):
    s = str(n)
    return s == s[::-1]

def pali_sum(n):
    square_list = []
    for k in range(1,int(math.sqrt(n))):
        square_list.append(k**2)
    pali_list = []
    for i in range(len(square_list) - 1):
        num = square_list[i] + square_list[i + 1]
        index = i + 2
        while num < n:
            if palindromic(num):
                if num not in pali_list:
                    pali_list.append(num)
            num += square_list[index]
            index += 1
    return sum(pali_list)

print(pali_sum(10**8))

#Answer = 2906969179

