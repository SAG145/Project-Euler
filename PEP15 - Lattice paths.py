def factorial(n):
    a = 1
    for i in range(1,n+1):
        a *= i
    return a

print(int(factorial(40)/(factorial(20)*factorial(20))))

#Answer = 137846528820

