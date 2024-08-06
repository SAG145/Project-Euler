list1 =[319,680,180,690,129,620,762,689,762,318,368,710,720,710,629,168,160,689,716,731,736,729,316,729,729,710,769,290,719,680,318,389,162,289,162,718,729,319,790,680,890,362,319,760,316,729,380,319,728,716]
lst = ['319', '680', '180', '690', '129', '620', '762', '689', '318', '368', '710', '720', '629', '168', '160', '716', '731', '736', '729', '316', '769', '290', '719', '389', '162', '289', '718', '790', '890', '362', '760', '380', '728']

def copy_str(lst1,lst2=[]):
    for i in lst1:
        if str(i) in lst2:
            None
        else:
            lst2.append(str(i))
    return lst2
#הרשימה lst זה מה שיוצא אחרי שמריצים את הפונקציה copy_str על list1

def copy(lst,lst1=[]):
    for i in lst:
        if i in lst1:
            None
        else:
            lst1.append(i)
    return lst1
list2 = []
for i in lst:
    list2.append([i[0],i[1]])
    list2.append([i[1], i[2]])
    list2.append([i[0], i[2]])
listba = copy(list2)

for l in listba:
    for m in listba:
        if l[1]==m[0]:
            if [str(l[0]),str(m[1])] in listba:
                listba.remove([str(l[0]),str(m[1])])
print(len(listba),listba)

#מכן עשיתי את זה על מחברת עם היגיון ובעזרת דיאגרמת Hesse
#answer = 73162890
