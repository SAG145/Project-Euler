def sum_digits_power_2(n,sum=0):
    while n>0:
        sum += (n%10)*(n%10)
        n = n//10
    return sum

def chain(n):
    if n==89:
        return 89
    elif n==1:
        return 1
    else:
        return chain(sum_digits_power_2(n))

x = 0
for i in range(1,10000000):
    if chain(i) == 89:
        x += 1
print(x)

#Answer = 8581146

