import math
def all_primes_below_n(n):
    primes_bool = [False, False] + [True] * (n - 2)
    for k in range(2, int(math.sqrt(n)) + 1):
        if primes_bool[k]:
            for l in range(2*k,n,k):
                primes_bool[l] = False
    primes_list = []
    for k in range(n):
        if primes_bool[k]:
            primes_list.append(k)
    return primes_list

def plus_1(t,i):
    if i == 0:
        return (t[0] + 1,t[1])
    return (t[0],t[1] + 1)

def bs_to_int(s):
    n = 0
    for i in range(len(s)):
        n += 2**i*int(s[i])
    return n

def clg(n):
    if n == 0:
        return 0
    return math.ceil(math.log(n,2))

def E(n):
    primes = all_primes_below_n(n)
    bin_nums = []
    max_log = math.ceil(math.log(n,2))
    for start in range(0,n):
        bin_nums.append([(0,0)]*(max_log - clg(start) + 1))

    for p in primes:
        b = bin(p)[2:][::-1]
        start = ""
        next = ""
        zeros = 0
        for i in range(-1,len(b) - 1):
            bsis = bs_to_int(start)
            if b[i + 1] == "1":
                bin_nums[bsis][zeros] = plus_1(bin_nums[bsis][zeros],1)
                zeros = 0
                next += "1"
                start = next
            else:
                bin_nums[bsis][zeros] = plus_1(bin_nums[bsis][zeros],0)
                zeros += 1
                next += "0"
    points = 0
    for bn in bin_nums:
        for b in bn:
            points += max(b)
    return points / len(primes)

print(round(10**8*E(10**8)) / 10**8)

#answer = 14.97696693
#זמן הרצה - רבע שעה