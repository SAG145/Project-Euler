def odd_digits(n):
    s = str(n)
    if "0" not in s and "2" not in s and "4" not in s and "6" not in s and "8" not in s:
        return True
    return False

def reverse(n):
    return int(str(n)[::-1])

def reversible(n):
    if n % 10 == 0:
        return False
    if odd_digits(n + reverse(n)):
        return True
    return False

reversibles = 0
for n in range(10**1,10**8):
    if reversible(n):
        reversibles += 1
print(reversibles)

#Answer = 608720

#Time: 1:30
#It is enough to check up to 10^8 because there are no reversible numbers with 9 digits.
