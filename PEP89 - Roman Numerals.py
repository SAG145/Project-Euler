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

def minimal_form(number):
    numerals = 0
    a = 0
    while number > 0:
        digit = number % 10
        if (digit == 4 or digit == 9):
            if a == 3:
                numerals += digit
            else:
                numerals += 2
        elif digit > 4:
            numerals += 1 + digit % 5
        else:
            numerals += digit
        number = number // 10
        a += 1
    return numerals

numerals_saved = 0
f = open("0089_roman.txt","r")
file = f.read() + "\n"
current_rom_num = ""
for ch in file:
    if ch == "\n":
        numerals_saved += len(current_rom_num) - minimal_form(roman_to_deci(current_rom_num))
        current_rom_num = ""
    else:
        current_rom_num += ch
print(numerals_saved)

#answer = 743
