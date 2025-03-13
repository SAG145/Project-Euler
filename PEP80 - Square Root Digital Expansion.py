import math

def sum_100_digits_sqrt(n):
    n1 = n*10**220
    guess = 0
    power_digit = 120
    while power_digit>-1:
        k = 0
        while k<10:
            if (guess + 10**power_digit)**2 < n1:
                guess += 10**power_digit
            k += 1
        power_digit -= 1
    sqrt = str(guess)[:100]
    sum = 0
    for i in sqrt:
        sum += int(i)
    return sum

x = 0
for num in range(100):
    if int(math.sqrt(num)) != math.sqrt(num):
        x += sum_100_digits_sqrt(num)
print(x)

#Answer = 40886

