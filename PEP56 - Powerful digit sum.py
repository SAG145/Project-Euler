def sumdigits(n,sum=0):
    while n>0:
        sum += n%10
        n = n//10
    return sum
x = 0
for i in range(1,100):
    for k in range(1,100):
        if sumdigits(i**k) > x:
            x = sumdigits(i**k)
print(x)
#answer = 972
