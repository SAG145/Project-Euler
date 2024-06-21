def first_3000_digits_fraction(n):
    return str(10**3010//n)[:3000]

def len_of_recurring_cycle_fraction(n):
    str1 = first_3000_digits_fraction(n)
    cycles_list = []
    len1 = len(str1) - 7
    for ch in range(len1):
        current_cycle = str1[ch:ch+5]
        if current_cycle in cycles_list:
            i = cycles_list.index(current_cycle)
            a = ch-i
            if str1[i:ch] == str1[ch:ch+a]:
                return a
        else:
            cycles_list.append(current_cycle)

max_cycle = 0
x = 0
for d in range(2,1001):
    if len_of_recurring_cycle_fraction(d) > max_cycle:
        max_cycle = len_of_recurring_cycle_fraction(d)
        x = d
print(x)

#answer = 983
