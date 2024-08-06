import math
def is_prime(n):
    if n % 2 == 0:
        return False
    for k in range(3,int(math.sqrt(n))+1,2):
        if n % k == 0:
            return False
    return True

def is_palindrom(num):
    s = str(num)
    if s == s[::-1]:
        return True
    return False

prime_lst = []
for i in range(3,10000000,2):
    if is_prime(i):
        prime_lst.append(i)

num_of_squ = 0
sum = 0
for p in prime_lst:
    squ = p**2
    if is_palindrom(squ) == False:
        uqs = int(str(squ)[::-1])
        if math.sqrt(uqs) % 1 == 0:
            if is_prime(int(math.sqrt(uqs))):
                sum += squ
                num_of_squ += 1
                print(squ)
k = 10000001
while num_of_squ != 50:
    if is_prime(k):
        squ = k**2
        if is_palindrom(squ) == False:
            uqs = int(str(squ)[::-1])
            if math.sqrt(uqs) % 1 == 0:
                if is_prime(int(math.sqrt(uqs))):
                    sum += squ
                    num_of_squ += 1
                    print(squ)
    k += 2
print(sum)
#answer = 3807504276997394
