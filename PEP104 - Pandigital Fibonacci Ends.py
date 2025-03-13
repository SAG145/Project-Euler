import sys

sys.set_int_max_str_digits(100000)

def pandigital_1_to_9(n):
    s = str(n)
    if len(set(s)) == 9:
        return "0" not in s

a = 102334155
b = 165580141
c = 0
last1_9_digits = 102334155
last2_9_digits = 165580141
mod = 10**9
index = 41
while True:
    c = a
    a = b
    b += c
    index += 1
    l = last1_9_digits
    last1_9_digits = last2_9_digits % mod
    last2_9_digits = (last2_9_digits + l) % mod
    if pandigital_1_to_9(last2_9_digits):
        if pandigital_1_to_9(str(b)[:9]):
            print(index)
            break

#Answer = 329468
