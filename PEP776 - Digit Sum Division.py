def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def F(N):
    str1 = str(N)
    l = len(str1)
    sum_digit_sum = [[0]*(9*l + 1),[0,1,2,3,4,5,6,7,8,9] + [0]*(9*l - 9)]
    num_digit_sum = [[0]*(9*l + 1),[1]*10 + [0]*(9*l - 9)]
    for i in range(2,l + 1):
        news = [0]*(9*l + 1)
        newn = [0]*(9*l + 1)
        for d in range(10):
            news[d] += d*10**(i - 1)
            for s in range(len(sum_digit_sum[-1])):
                if sum_digit_sum[-1][s] != 0:
                    news[s + d] += d*10**(i - 1)*num_digit_sum[-1][s] + sum_digit_sum[-1][s]
                if num_digit_sum[-1][s] != 0:
                    newn[s + d] += num_digit_sum[-1][s]
        newn[0] = 1
        sum_digit_sum.append(news)
        num_digit_sum.append(newn)

    sigma = N / digit_sum(N)
    for i in range(l):
        pre1 = str1[:i]
        l1 = l - i - 1
        for e in range(int(str1[i])):
            pre2 = pre1 + str(e)
            t = digit_sum(int(pre2))
            for ds in range(len(sum_digit_sum[l1])):
                if ds != 0:
                    sigma += (int(pre2)*10**(l1)*num_digit_sum[l1][ds] + sum_digit_sum[l1][ds]) / (ds + t)
                elif t != 0:
                    sigma += int(pre2)*10**l1 / t

    return sigma

s = str(F(1234567890123456789))
print(str(round(float(s[:s.index("e")]),12)) + "e" + s[-2:])

#Answer = 9.627509725002e33