def sumdigits(n,sum=0):
    while n>0:
        sum += n%10
        n = n//10
    return sum
print(sumdigits(2**1000))
#answer = 1366
