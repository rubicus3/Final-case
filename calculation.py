from math import *
import requests


def A2B(F_Point, Electr_Points):
    Gen = 8
    SHs, Distance = F_Point
    Days = 0
    Results = []
    Credits = 0
    while Distance > 0:
        Days += 1
        k_Growth = sin(degrees(-pi / 2 + pi * (Temp + 0.5 * Oxygen)))
        Gen += Gen * k_Growth  # G
        if Gen < 8:
            Gen = 0
            break
        Mass = 192 + Gen  # M
        Electr_Points += Electr_Power * 11 #
        Velocity = 2 * (Reactor_Power / 80) * (200 / Mass)
        Elect_f_supp = sum(range(0, Temp))# E(T)
        Distance -= Velocity
        Credits += Reactor_Power * 10 + Oxygen * 7
        Results.append({f"{Days}": [Distance, Gen, Credits]})
    return Results


headers = {"X-Auth-Token": "2u3jct64"}
r = requests.get('https://dt.miet.ru/ppo_it_final', headers=headers)
F_Points = r.json()['message']

# 1 oxygen = 7 credits
# 1 fuel = 10 credits


F_Points = []
Reactor_Power = 0  # 1 fuel = 1%  W + E
Engine_Power = 0  # W = max 80%
Electr_Power = 0 # E
Days = 0
Oxygen = 0  # Oxi
Temp = 0  # T e [0;30]°C
Gen = 8  # G
Electr_Points = 0

