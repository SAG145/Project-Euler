def factorial(n,mult=1):
    for i in range(2,n+1):
        mult *= i
    return mult

def sum_digits_factorials(n,sum=0):
    while n>0:
        sum += factorial((n%10))
        n = n//10
    return sum
x = 0
for k in range(3,3000000):
    if sum_digits_factorials(k) == k:
        x += k
print(x)
#answer = 40730
