def sum_digits_power_5(n,sum=0):
    while n>0:
        sum += (n%10)**5
        n = n//10
    return sum

x = 0
for i in range(2,354294): #354294 = 6*9**5
    if i==sum_digits_power_5(i):
        x += i
print(x)
#answer = 443839