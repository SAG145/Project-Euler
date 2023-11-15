import random
cc_squares = [2,17,33]
ch_squares = [7,22,36]
cc_go_to = [0,10] + [None]*14
ch_go_to = [0,5,10,11,24,39,-1,-1,-2,-3] + [None]*6
squares_list = [0]*40

def copy_list(lst):
    lst1 = []
    for k in lst:
        lst1.append(k)
    return lst1

def card_to_buttom(lst):
    lst1 = copy_list(lst)
    for k in range(len(lst)-1):
        lst[k] = lst1[k+1]
    lst[len(lst1)-1] = lst1[0]
    return lst

def random_list(lst):
    len1 = len(lst)
    lst1 = []
    for k in range(len1):
        r = random.randint(0,len(lst)-1)
        lst1.append(lst[r])
        lst.pop(r)
    return lst1

def max_lst_index(lst):
    maxi = 0
    for k in range(len(lst)):
        if lst[k] > lst[maxi]:
            maxi = k
    return maxi

def turn(current_square,cc_squares,ch_squares,cc_go_to,ch_go_to,doubles):
    c1 = random.randint(1,4)
    c2 = random.randint(1,4)
    if c1 == c2:
        if doubles == 2:
            current_square = 10
        else:
            doubles += 1
            current_square = (current_square + c1 + c2) % 40
    else:
        doubles = 0
        current_square = (current_square + c1 + c2) % 40
    if current_square == 30:
        current_square = 10
    elif current_square in cc_squares:
        if cc_go_to[0] == 0:
            current_square = 0
        elif cc_go_to[0] == 10:
            current_square = 10
        cc_go_to = card_to_buttom(cc_go_to)
    elif current_square in ch_squares:
        if type(ch_go_to[0]) == int:
            if ch_go_to[0] > -1:
                current_square = ch_go_to[0]
            else:
                if ch_go_to[0] == -1:
                    if current_square == 7:
                        current_square = 15
                    elif current_square == 22:
                        current_square = 25
                    else:
                        current_square = 5
                elif cc_go_to[0] == -2:
                    if current_square == 22:
                        current_square = 28
                    else:
                        current_square = 12
                else:
                    current_square -= 3
        ch_go_to = card_to_buttom(ch_go_to)

    return [current_square,doubles]

for p in range(5):
    a = 0
    doubles = 0
    ch_go_to = random_list(ch_go_to)
    cc_go_to = random_list(cc_go_to)
    for k in range(100000):
        d = doubles
        b = turn(a,cc_squares,ch_squares,cc_go_to,ch_go_to,doubles)
        a = b[0]
        doubles = b[1]
        if d == doubles:
            squares_list[a] += 1

final_string = ""
lst1 = copy_list(squares_list)
for i in range(3):
    j1 = max_lst_index(lst1)
    j2 = squares_list.index(lst1[j1])
    if j2 < 10:
        final_string += "0" + str(j2)
    else:
        final_string += str(j2)
    lst1.pop(j1)
print(int(final_string))

#answer = 101524