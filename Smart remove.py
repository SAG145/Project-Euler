def smart_remove(lst):
    i = 0
    while i<len(lst):
        if "Insert a condition here":
            lst.pop(i)
        else:
            i += 1


#demonstration:

lst1 = []
lst2 = []
for i in range(1000):
    lst1.append(i)
    lst2.append(i)

for x in lst1:
    if x%3 == 0 or x%2 == 0:
        lst1.remove(x)

i = 0
while i<len(lst2):
    if lst2[i]%3 == 0 or lst2[i]%2 == 0:
        lst2.pop(i)
    else:
        i += 1

print(lst1)
print(lst2)
print(lst1==lst2)