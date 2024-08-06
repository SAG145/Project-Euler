from math import factorial
import copy
def digits_to_digits_sum(digits):
    digits_sum = 0
    for d in range(1,10):
        digits_sum += d*digits[d]
    return digits_sum

def sums(list1,digits,i):
    if sum(digits) == 10:
        list1[digits_to_digits_sum(digits)].append(digits)
    else:
        for d in range(i,10):
            if digits[d] < 2:
                dig = copy.copy(digits)
                dig[d] += 1
                sums(list1,dig,d)

def factorial_list(lst):
    m = 1
    for k in lst:
        m *= factorial(k)
    return m

def permutation_with_leading_zeros(digits):
    return factorial(sum(digits)) // factorial_list(digits)

def permutation_without_leading_zeros(digits):
    return permutation_with_leading_zeros(digits)*(sum(digits) - digits[0]) // sum(digits)

def double_pandigital(dig1,dig2):
    for d in range(10):
        if dig1[d] + dig2[d] != 2:
            return False
    return True

sums_nums = []
for k in range(91):
    sums_nums.append([])
sums(sums_nums,[0]*10,0)

double_pand_divi_11 = 0
for i in range(1,71):
    if (90 - 2*i) % 11 == 0:
        if sums_nums[i] != [] and sums_nums[90 - i] != []:
            for p1 in sums_nums[i]:
                for p2 in sums_nums[90 - i]:
                    if double_pandigital(p1,p2):
                        double_pand_divi_11 += permutation_with_leading_zeros(p1)*permutation_without_leading_zeros(p2)

print(double_pand_divi_11)

#answer = 194505988824000
