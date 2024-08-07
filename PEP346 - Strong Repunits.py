import math
def sum_of_strong_repunits(maxi):
    strong_repunits_nums = [1]
    for k in range(2,int(math.sqrt(maxi))+1):
        power_digit = 3
        num = k**2 + k + 1
        while num < maxi:
            if num not in strong_repunits_nums:
                strong_repunits_nums.append(num)
            num += k**power_digit
            power_digit += 1
    return sum(strong_repunits_nums)

print(sum_of_strong_repunits(10**12))

#answer = 336108797689259276
#זמן ריצה - שעה וחצי
