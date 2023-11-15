import math
file = open("0099_base_exp.txt","r")
s = str(file.read())
s += "\n" + "s"
power_list = []
current_base = ""
current_exp = ""
for char in s:
    if char == ",":
        current_base = int(current_base)
    elif char == "\n":
        power_list.append(math.log(current_base,1000)*int(current_exp))
        current_base = ""
        current_exp = ""
    else:
        if type(current_base) == int:
            current_exp += char
        else:
            current_base += char

max_element = 0
for i in range(1000):
    if power_list[i] > max_element:
        max_element = power_list[i]
        max_index = i
print(max_index+1)

#answer = 709