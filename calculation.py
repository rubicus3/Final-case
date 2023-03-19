from math import *


Reactor_Power = 0  # 1 fuel = 1%
Engine_Power = 0  # W = max 80%
Electr_Power = 0
Days = 0
Mass = 1
Oxygen = 0
Temp = 0
Gen = 0

k_Growth = sin(radians(-pi / 2 + pi * (Temp + 0.5 * Oxygen)))
Electr_Points = Electr_Power * Days * 11
Gen += Gen * k_Growth