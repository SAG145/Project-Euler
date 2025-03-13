def neto_bin_str(n):
    return str(bin(n))[2:]

x = 0
for i in range(1000000):
    if neto_bin_str(i) == neto_bin_str(i)[::-1] and str(i) == str(i)[::-1]:
        x += i
print(x)

#Answer = 872187

