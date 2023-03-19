from math import *
import requests


def A2B(F_Point):
    Days = 0
    Gen = 8
    SHs, Distance = F_Point
    Days_min = []
    Amin = 100000000000
    for Temp in range(0, 31):
        for Oxygen in range(1, 61):
            Results = {}
            Days = 0
            Engine_Power = 80
            Reactor_Power = 85
            while Distance > 0:
                Days += 1
                k_Growth = sin(degrees(-pi / 2 + pi * (Temp + 0.5 * Oxygen)))
                Gen += Gen * k_Growth  # G
                if Gen < 8:
                    Gen = 0
                    break
                Mass = 192 + Gen  # M
                Velocity = 2 * (Engine_Power / 80) * (200 / Mass)
                Distance -= Velocity
                Credits = Reactor_Power * 10 + Oxygen * 7

                Results.update({f"{Days}": [Distance, Gen, Credits]})
            if Days < Amin and Days:
                Amin = Days
                Days_min = Results
    return Amin, Days_min


# 1 oxygen = 7 credits
# 1 fuel = 10 credits
def alaka():
    headers = {"X-Auth-Token": "2u3jct64"}
    r = requests.get('https://dt.miet.ru/ppo_it_final', headers=headers)
    F_Points = r.json()['message']
    a = []
    for i in F_Points:
        a.append(sorted([A2B((j['SH'], j['distance'])) for j in i['points']], key=lambda x: x[0])[0])
    return a



Reactor_Power = 0  # 1 fuel = 1%  W + E
Engine_Power = 0  # W = max 80%
Electr_Power = 0  # E
Days = 0
Oxygen = 0  # Oxi
Temp = 0  # T e [0;30]°C
Gen = 8  # G
Electr_Points = 0
