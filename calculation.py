from math import *
import requests

headers = {"X-Auth-Token": "2u3jct64"}
r = requests.get('https://dt.miet.ru/ppo_it_final', headers=headers)
print(r.json()['message'])



Reactor_Power = 0  # 1 fuel = 1%
Engine_Power = 0  # W = max 80%
Electr_Power = 0
Days = 0
Mass_Const = 192  # M without SH
Oxygen = 0  # Oxi
Temp = 0  # T e [0;30]°C
Gen = 0  # G
Elect_f_supp = sum(range(0, Temp))# E(T)



# Calculations
k_Growth = sin(degrees(-pi / 2 + pi * (Temp + 0.5 * Oxygen)))
Electr_Points = Electr_Power * Days * 11 #
Gen += Gen * k_Growth # G
if Gen < 8:
    Gen = 0
Mass = Mass_Const + Gen # M
#Energy_Temp  # E(T)
