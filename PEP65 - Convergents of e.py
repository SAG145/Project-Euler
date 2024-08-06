def sum_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

a1 = 2
a2 = 3
even = 2
convergent = 2
while convergent<100:
    x = a1
    y = a2
    if (convergent + 1 ) % 3 == 0:
        a1 = y
        a2 = x + y*even
        convergent += 1
        even += 2
    else:
        a1 = y
        a2 = x + y
        convergent += 1
print(sum_digits(a2))

#answer = 272
