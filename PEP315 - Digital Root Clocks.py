import math
def all_primes_m_to_n(m,n):
    primes_bool = [False, False] + [True] * (n - 2)
    for k in range(2, int(math.sqrt(n)) + 1):
        if primes_bool[k]:
            for l in range(2*k,n,k):
                primes_bool[l] = False
    primes_list = []
    for k in range(m,n):
        if primes_bool[k]:
            primes_list.append(k)
    return primes_list

def e_magniv(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

def saving_step(n):
    saving = 0
    target = e_magniv(n)
    while target > 0:
        saving += num_of_1(and_bin(target % 10,n % 10))
        target = target // 10
        n = n // 10
    return 2*saving

def num_of_1(str1):
    one = 0
    for ch in str1:
        if ch == "1":
            one += 1
    return one

def and_bin(d1,d2):
    b1 = digital_list[d1]
    b2 = digital_list[d2]
    final = ""
    for k in range(7):
        if b1[k] == "1" and b2[k] == "1":
            final += "1"
        else:
            final += "0"
    return final

def final_saving(n,s = 0):
    if n < 65:
        return s + saving[n]
    if n < 10:
        return s
    return final_saving(e_magniv(n),s + saving_step(n))

digital_list = ["1110111","0010010","1011101","1011011","0111010","1101011","1101111","1110010","1111111","1111011"]
saving = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 8, 6, 6, 10, 6, 8, 12, 18, 8, 4, 4, 8, 6, 6, 12, 8, 18, 8, 8, 4, 6, 8, 6, 10, 10, 16, 10, 20, 6, 2, 8, 6, 8, 10, 18, 10, 22, 20, 8, 2, 4, 10, 8, 14, 6, 14, 18, 16, 10, 4, 10, 10, 12]
primes = all_primes_m_to_n(10**7,2*10**7)
x = 0
for p in primes:
    x += final_saving(p)
print(x)

#answer = 13625242
