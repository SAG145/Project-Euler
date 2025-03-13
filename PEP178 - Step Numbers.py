def step(start_both,start_none,start_zero,start_nine,current_number,current_len,max_len,zero,nine):
    last_digit = int(current_number[-1])
    if last_digit == 0:
        zero = True
    elif last_digit == 9:
        nine = True
    if current_len == max_len:
        if zero and nine:
            start_both[10 * int(current_number[0]) + int(current_number[-1])] += 1
        elif zero:
            start_zero[10*int(current_number[0]) + int(current_number[-1])] += 1
        elif nine:
            start_nine[10*int(current_number[0]) + int(current_number[-1])] += 1
        else:
            start_none[10 * int(current_number[0]) + int(current_number[-1])] += 1
    else:
        if last_digit == 0:
            step(start_both,start_none,start_zero,start_nine,current_number + "1",current_len + 1,max_len,zero,nine)
        elif last_digit == 9:
            step(start_both,start_none,start_zero,start_nine, current_number + "8", current_len + 1, max_len,zero,nine)
        else:
            step(start_both,start_none,start_zero,start_nine, current_number + str(last_digit + 1), current_len + 1, max_len,zero,nine)
            step(start_both,start_none,start_zero,start_nine, current_number + str(last_digit - 1), current_len + 1, max_len,zero,nine)

def num_of_pan_step_len(len1):
    if len1 % 2 != 0:
        s = 0
        start_both1 = [0] * 100
        start_zero1 = [0] * 100
        start_nine1 = [0] * 100
        start_none1 = [0] * 100
        start_both2 = [0] * 100
        start_zero2 = [0] * 100
        start_nine2 = [0] * 100
        start_none2 = [0] * 100
        for d in range(10):
            step(start_both1, start_none1, start_zero1, start_nine1, str(d), 1, len1 // 2, False, False)
            step(start_both2, start_none2, start_zero2, start_nine2, str(d), 1, len1 // 2 + 1, False, False)
        for a in range(10, 100):
            m = a % 10
            if m == 0:
                lst = [1]
            elif m == 9:
                lst = [8]
            else:
                lst = [m - 1, m + 1]
            for b in lst:
                c = b * 10
                for d in range(10):
                    s += start_both1[a]*start_none2[c + d] + start_both1[a]*start_nine2[c + d] + start_both1[a]*start_zero2[c + d] + start_both1[a]*start_both2[c + d]
                    s += start_zero1[a]*start_nine2[c + d] + start_zero1[a]*start_both2[c + d]
                    s += start_nine1[a]*start_zero2[c + d] + start_nine1[a]*start_both2[c + d]
                    s += start_none1[a]*start_both2[c + d]
        return s
    else:
        s = 0
        start_both = [0] * 100
        start_zero = [0] * 100
        start_nine = [0] * 100
        start_none = [0] * 100
        for d in range(10):
            step(start_both, start_none, start_zero, start_nine, str(d), 1, len1 // 2, False, False)
        for a in range(10,100):
            m = a % 10
            if m == 0:
                lst = [1]
            elif m == 9:
                lst = [8]
            else:
                lst = [m - 1,m + 1]
            for b in lst:
                c = b*10
                for d in range(10):
                    s += start_both[a] * start_none[c + d] + start_both[a] * start_nine[c + d] + start_both[a] * start_zero[c + d] + start_both[a] * start_both[c + d]
                    s += start_zero[a] * start_nine[c + d] + start_zero[a] * start_both[c + d]
                    s += start_nine[a] * start_zero[c + d] + start_nine[a] * start_both[c + d]
                    s += start_none[a] * start_both[c + d]
        return s

pan_step_nums = 1
for k in range(11,41):
    a = num_of_pan_step_len(k)
    pan_step_nums += a
print(pan_step_nums)

#Answer = 126461847755

