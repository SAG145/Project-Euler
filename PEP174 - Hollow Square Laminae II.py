import math

t_list = [0]*(10**6 + 1)
for k in range(3,500002):
    if k > 1000:
        a = int(math.sqrt(k**2 - 1000000 - 1)) + 1
        if a % 2 == 0:
            for l in range(a + k % 2,k - 1,2):
                t_list[k**2 - l**2] += 1
        else:
            for l in range(a + 1 - k % 2,k - 1,2):
                t_list[k**2 - l**2] += 1
    else:
        for l in range(2 - k % 2,k - 1,2):
            t_list[k**2 - l**2] += 1
x = 0
for k in t_list:
    if k < 11 and k > 0:
        x += 1
print(x)

#answer = 209566
