mod_fib = [1,1,2,4]
perm_part_2 = [1,2,4,9]
spp2 = [1,3,7,16]

n = 3
mod = 1000000
while True:
    mod_fib.append((mod_fib[-1] + mod_fib[-2] + mod_fib[-4]) % mod)
    perm_part_2.append((spp2[-1] + mod_fib[n]) % mod)
    spp2.append(spp2[-1] + perm_part_2[-1])
    if n % 2 == 0:
        t1 = perm_part_2[(n - 4) // 2] + pow(2,(n - 2) // 2 - 1,1000000) + spp2[(n - 8) // 2]
    else:
        t1 = spp2[(n - 5) // 2]
    if t1 % mod == 0 and n > 42:
        print(n)
        break
    n += 1

#Answer = 1275000

#I wrote a function that calculates the number of permutations of the divisors of n, and the number of permutations of the divisors of n that contain 2.
#Then I noticed the regularity that the number of permutations of the divisors of n is 2 to the power of n - 1.
#And the number of permutations of the divisors of n that contain 2 obeys some regularity, which I was able to identify.
#Based on these I eventually wrote the code.
