def ch_to_dec(ch):
    return ord(ch) - 65

def dec_to_ch(dec):
    return chr(dec + 65)

def swap(s,i,j):
    return s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]

def next_perm(s):
    i1 = -1
    i2 = -1
    for j in range(len(s) - 2,-1,-1):
        if s[j] < s[j + 1]:
            i1 = j
            break
    for k in range(len(s) - 1,-1,-1):
        if s[k] > s[i1]:
            i2 = k
            break
    s = swap(s,i1,i2)
    return s[:i1 + 1] + s[i1 + 1:len(s)][::-1]

def num_of_rots(arr):
    rots = 0
    for i in range(len(arr)):
        if ch_to_dec(arr[i]) != i:
            j = arr.index(dec_to_ch(i))
            if j != len(arr) - 1:
                arr = arr[:j] + arr[j:][::-1]
                rots += 1
            arr = arr[:i] + arr[i:][::-1]
            rots += 1
    return rots


arr = "BACDEFGHIJK"
maximix = 0
while maximix != 2011:
    arr = next_perm(arr)
    if num_of_rots(arr) == 19:
        maximix += 1

print(arr)

#Answer = CAGBIHEFJDK