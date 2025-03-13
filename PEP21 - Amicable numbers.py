def divisors_sum(n):
    sum = 0
    for i in range(1,n//2+1):
        if n%i==0:
            sum += i
    return sum

sum = 0
for i in range(10000):
    x = divisors_sum(i)
    if divisors_sum(x) == i and i<10000 and x<10000 and i!=x:
        sum += x + i
print(sum/2)

#Answer = 31626
