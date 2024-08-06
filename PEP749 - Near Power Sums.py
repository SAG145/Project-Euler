def power_list(lst,power):
    s = 0
    for n in range(10):
        if lst[n] != 0:
            s += lst[n]*n**power
    return s

def num_to_digits(num):
    dig = [0]*10
    for k in str(num):
        dig[int(k)] += 1
    return dig

def only_ones_or_zeros(digits):
    # if digits[0]*digits[1] != 0:
    #     return False
    for k in range(2,10):
        if digits[k] != 0:
            return False
    return True

def near_power_sum(digits):
    k = sum(digits) - 1
    if sum(digits) < 2:
        return -1
    if only_ones_or_zeros(digits):
        return -1
    while True:
        power_k = power_list(digits,k)
        d1 = num_to_digits(power_k - 1)
        if sum(d1) > sum(digits):
            break
        if d1 == digits:
            return power_k - 1
        if num_to_digits(power_k + 1) == digits:
            return power_k + 1
        k += 1
    return -1

def S(d):
    s = 0
    for d0 in range(d):
        for d1 in range(d - d0 + 1):
            for d2 in range(d - d0 - d1 + 1):
                for d3 in range(d - d0 - d1 - d2 + 1):
                    for d4 in range(d - d0 - d1 - d2 - d3 + 1):
                        for d5 in range(d - d0 - d1 - d2 - d3 - d4 + 1):
                            for d6 in range(d - d0 - d1 - d2 - d3 - d4 - d5 + 1):
                                for d7 in range(d - d0 - d1 - d2 - d3 - d4 - d5 - d6 + 1):
                                    for d8 in range(d - d0 - d1 - d2 - d3 - d4 - d5 - d6 - d7 + 1):
                                        for d9 in range(d - d0 - d1 - d2 - d3 - d4 - d5 - d6 - d7 - d8 + 1):
                                            digits = [d0,d1,d2,d3,d4,d5,d6,d7,d8,d9]
                                            if digits != [0]*10:
                                                if near_power_sum(digits) != -1:
                                                    s += near_power_sum(digits)
    return s

print(S(16))

#answer = 13459471903176422
#זמן הרצה - דקה וחצי
