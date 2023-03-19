from typing import Optional, List

from pydantic import BaseModel



class Day(BaseModel):
    day_num: Optional[int]
    engine_percent: Optional[int] # процент мощности реатора на двигатель
    electr_percent: Optional[int] # процент мощности реатора на электричество
    autoclav_temp: Optional[int] # температура в автоклаве
    sh: Optional[int]
    spend_fuel: Optional[int]
    spend_oxi: Optional[int]

    remain_fuel: Optional[int] # для точек выгрузки
    remain_oxi: Optional[int] # для точек выгрузки