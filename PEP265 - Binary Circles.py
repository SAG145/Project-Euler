def circular(str,len1):
    l = len(str)
    subsequences = []
    for k in range(l):
        s = ""
        for i in range(len1):
            s += str[(k + i) % l]
        if s in subsequences:
            return False
        subsequences.append(s)
    return True

def S(n):
    s = "0"*n
    sum = 0
    for k in range(2**(2**n - n - 1) + 1,2**(2**n - n),1):
        if circular(s+bin(k)[2:],n):
            sum += k
    return sum

print(S(5))

#Answer = 209110240768

