from math import *
import requests

headers = {"X-Auth-Token": "2u3jct64"}
r = requests.get('https://dt.miet.ru/ppo_it_final', headers=headers)
print(r.json()['message'])


# 1 oxygen = 7 credits
# 1 fuel = 10 credits


F_Points = [r[0]]
Reactor_Power = 0  # 1 fuel = 1%
Engine_Power = 0  # W = max 80%
Electr_Power = 0
Days = 0
Mass_Const = 192  # M without SH
Oxygen = 0  # Oxi
Temp = 0  # T e [0;30]°C
Gen = 0  # G



# Calculations
Electr_Points = Electr_Power * Days * 11 #
Elect_f_supp = sum(range(0, Temp))# E(T)
Velocity = 2 * (Reactor_Power / 80) * (200 / Mass)



#Flight
for F_Point in F_Points:
    SHs, Distance = F_Point
    while Distance > 0:
        k_Growth = sin(degrees(-pi / 2 + pi * (Temp + 0.5 * Oxygen)))
        Gen += Gen * k_Growth  # G
        if Gen < 8:
            Gen = 0
    Mass = Mass_Const + Gen  # M
