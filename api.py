from schemas import Day
from calculation import alaka

def f():
    a = alaka()
    lst = a[1]
    v = []
    for i in lst.keys():
        v.append(Day(day_num=i, sh=lst[i][1]))
    return v

def g():
    a = alaka()
    b = a[0]
    return b