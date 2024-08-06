import math
def prime(n):
    a = True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            a = False
            break
    return a

def prime_factors(n):
    prime_list = []
    i = 2
    while n>1:
        if n%i == 0:
            if prime(i):
                if i in prime_list:
                    None
                else:
                    prime_list.append(i)
                n = n/i
        else:
            i += 1
    return prime_list
i = 1
while 1>0:
    if len(prime_factors(i)) == 4:
        if len(prime_factors(i+1)) == 4:
            if len(prime_factors(i+2)) == 4:
                if len(prime_factors(i + 3)) == 4:
                    print(i)
                    break
                else:
                    i += 4
            else:
                i += 3
        else:
            i += 2
    else:
        i += 1
#answer = 134043
