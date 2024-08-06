import math
def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for k in range(3,int(math.sqrt(n))+1,2):
        if n % k == 0:
            return False
    return True

def long_division_9(prime):
    sum_of_digits = 0
    nine = prime - 1
    num_of_9 = 0
    current_num = 9
    while num_of_9 < nine:
        new_digit = current_num // prime
        sum_of_digits += new_digit
        current_num = 10*(current_num - prime*new_digit) + 9
        num_of_9 += 1
    return sum_of_digits

# lst = []
# for k in range(72*10**7 + 9891, 73*10**7 + 100,100000):
#     if is_prime(k):
#         lst.append(k)
#         print(k)
#         print(99999999999999999999999 / k) #השתמשתי בלולאה הזאת בשביל לבדוק איזה מספרים ראשוניים מקיימים את התנאיםת כלומר ...999999 חלקיהם בתחיל ב 137
# הם גדולים מ 10 בחזקת 8, ובנוסף חמשת הספרות האחרונות שלהם כפול 56789 מודולו 100000 יוצא 99999, מה שהוביל לזה שהם נגמרים ב 09891

# print(lst[2:])

# print(long_division_9(725509891))
# print(long_division_9(726509891)) #לאחר הרצת הלולאה יצאו שלושת המספרים האלה, לכל אחד מהם בדקתי בנפרד האם הוא זה שמוביל לפתרון ובסוף צדקתי
print(long_division_9(729809891))

#answer = 3284144505
