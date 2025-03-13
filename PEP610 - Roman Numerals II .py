def value(numeral):
    if numeral == "I":
        return 1
    if numeral == "V":
        return 5
    if numeral == "X":
        return 10
    if numeral == "L":
        return 50
    if numeral == "C":
        return 100
    if numeral == "D":
        return 500
    return 1000

def roman_to_deci(rom_num):
    number = value(rom_num[-1])
    numeral = 0
    while numeral < len(rom_num) - 1:
        num = value(rom_num[numeral])
        if num < value(rom_num[numeral + 1]):
            if numeral == len(rom_num) - 2:
                number -= value(rom_num[numeral + 1])
            number += value(rom_num[numeral + 1]) - num
            numeral += 2
        else:
            number += num
            numeral += 1
    return number

def deci_to_min_roman(num):
    rom = "M"*(num // 1000)
    num %= 1000
    s = str(num)
    s = "0"*(3 - len(s)) + s
    if s[0] <= "3":
        rom += "C"*int(s[0])
    elif s[0] == "4":
        rom += "CD"
    elif s[0] < "9":
        rom += "D" + "C"*(int(s[0]) - 5)
    else:
        rom += "CM"

    if s[1] <= "3":
        rom += "X"*int(s[1])
    elif s[1] == "4":
        rom += "XL"
    elif s[1] < "9":
        rom += "L" + "X"*(int(s[1]) - 5)
    else:
        rom += "XC"

    if s[2] <= "3":
        rom += "I"*int(s[2])
    elif s[2] == "4":
        rom += "IV"
    elif s[2] < "9":
        rom += "V" + "I"*(int(s[2]) - 5)
    else:
        rom += "IX"

    return rom

def is_min_form(rom_num):
    return rom_num == deci_to_min_roman(roman_to_deci(rom_num))

def chance(num):
    c = 1
    target = deci_to_min_roman(num)
    curr = ""
    for numeral in target:
        valids = 0
        for ch in "MDCLXVI":
            if is_min_form(curr + ch):
                valids += 1
        c *= 0.14*(1 / (0.14*valids + 0.02))
        curr += numeral

    valids = 0
    for ch in "MDCLXVI":
        if is_min_form(curr + ch):
            valids += 1
    c *= 0.02*(1 / (0.14 * valids + 0.02))
    return c

chances = [0.02]
for n in range(1,1000):
    chances.append(chance(n))

expected = 0
for i in range(20000):
    expected += i*0.14**(i // 1000)*chances[i % 1000]

print(round(expected,8))

#Answer = 319.30207833
