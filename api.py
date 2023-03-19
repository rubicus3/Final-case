from schemas import Day
from calculation import alaka

def f():
    a = alaka()
    lst = a[1]
    v = []
    print(lst)
    c = 0
    for i in lst[1]:
        c += 1
        v.append(Day(day_num=c, sh=i[str(c)][0], spend_oxi=i[str(c)][-1], autoclav_temp=i[str(c)][-3]))
    return v

def g():
    a = alaka()
    b = a[0][0]
    return b