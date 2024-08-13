def max_power_4(n):
    a = 1
    p = 1
    while n >= a:
        a *= 4
        p += 1
    return (a // 4,p - 1)

def dec_to_quat(n,l = 3):
    num = ""
    mp4 = max_power_4(n)
    p = mp4[0]
    m = mp4[1]
    while n != 0:
        num += str(n // p)
        n -= p*(n // p)
        p //= 4
    num = num + "0"*(m - len(num))
    if l != -1:
        return "0"*(l - len(num)) + num
    return num
def contained(s1,s2):
    for i in range(len(s2) - len(s1) + 1):
        if s2[i:i + len(s1)] == s1:
            return True
    return False

def score(word):
    sc = [0]*4
    if contained("FREE",word):
        sc[0] = 1
    if contained("FARE",word):
        sc[1] = 1
    if contained("AREA",word):
        sc[2] = 1
    if contained("REEF",word):
        sc[3] = 1
    return sc

def num_to_word(num):
    letters = ["A","E","F","R"]
    word = ""
    for d in dec_to_quat(num):
        word += letters[int(d)]
    return word

def plus_lists(lst1,lst2):
    plus = [0]*len(lst1)
    for i in range(len(lst1)):
        plus[i] += lst1[i] + lst2[i]
    return plus

def num_to_bin_list(n,l = 4):
    lst = []
    for b in bin(n)[2:]:
        lst.append(int(b))
    return [0]*(4 - len(lst)) + lst

def bin_list_to_dec(lst):
    n = 0
    lst = lst[::-1]
    for i in range(len(lst)):
        n += lst[i]*2**i
    return n

def next_three_letters(poss):
    new = []
    for i in range(64):
        new.append([0]*16)
    for w in range(64):
        word = num_to_word(w)
        for v in range(64):
            sc = score(word + num_to_word(v))
            for s in range(16):
                new_score = plus_lists(sc,num_to_bin_list(s))
                if max(new_score) < 2:
                    new[v][bin_list_to_dec(new_score)] += poss[w][s]
    return new

poss = []
for i in range(64):
    poss.append([1] + [0]*15)

for next in range(9):
    poss = next_three_letters(poss)

s = 0
for p in poss:
    s += p[-1]
print(s)

#answer = 644997092988678