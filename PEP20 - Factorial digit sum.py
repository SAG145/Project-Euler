def hhh(n,i=1):
    for k in range(1,n+1):
        i *= k
    return i

def sumdigits(n,sum=0):
    while n>0:
        sum += n%10
        n = n//10
    return sum

print(sumdigits(hhh(100)))
#answer = 648
