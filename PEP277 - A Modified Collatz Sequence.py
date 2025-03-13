sequence = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"

def func(num,mod,sequence,index):
    for i in range(index - 1):
        if sequence[i] == "D":
            num = num // 3
        elif sequence[i] == "d":
            num = ((2*num - 1) % mod) // 3
        else:
            num = ((4*num + 2) % mod) // 3
    lst = ["D","U","d"]
    return lst[num % 3] == sequence[index - 1]

def mod(sequence,power,reminder):
    m = 3**power
    poss = []
    for k in range(reminder,m,m // 3):
        poss.append(k)
    for p in poss:
        if func(p,m,sequence,power):
            return p

def final(sequence):
    r = mod(sequence,1,0)
    for i in range(2,len(sequence) + 1):
        r = mod(sequence,i,r)
    return r

x = final(sequence)
while x < 10**15:
    x += 3**30
print(x)

#Answer = 1125977393124310

