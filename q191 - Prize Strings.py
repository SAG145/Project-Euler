def fib3(n, values, index):
    if index + 1 > n:
        return values[n + 1]
    else:
        return fib3(n - 1, values, index) + fib3(n - 2, values, index) + fib3(n - 3, values, index)


def prize_strings(days):
    values = [1, 1, 2]
    index = 1
    for k in range(2, days + 1):
        values.append(fib3(k, values, index))
        index += 1
    sum = fib3(days, values, index) + 2 * fib3(days - 1, values, index)
    for index_l in range(1, days // 2):
        sum += 2 * fib3(index_l, values, index) * fib3(days - index_l - 1, values, index)
    return sum
print(prize_strings(30))

#answer = 1918080160