from typing import List

from kivy import Config
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable

from api import f, g

from schemas import Day

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Window.size = (1280, 720)


class Container(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.filled = False

        self.data_tables = MDDataTable(
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(0.9, 0.6),
            padding=10,
            use_pagination=True,
            column_data=[
                ("День", dp(30)),
                ("Оставшиеся  ресурсы", dp(40)),
                ("Расходумемые ресурсы", dp(40)),
                ("Распределение мощности реактора", dp(40)),
                ("Характеристика автоклава", dp(40)),
                ("Популяция SH", dp(40)),
            ],
            row_data=[("0", "0", "0", "0", "0", "0") for i in range(0)],
        )
        self.add_widget(self.data_tables)
        self.ids["label"].text = f"Количество дней: {0}"

    def update_days(self, days):
        self.ids["label"].text = f"Количество дней: {days}"

    def fill_rows(self, data: List[Day]):
        c = 0
        for i in data:
            c += 1
            d = (str(i.day_num), str(f"Топливо {i.remain_fuel} / Кислород {i.remain_oxi}"),
                 str(f"Топливо {i.spend_fuel} / Кислород {i.spend_oxi}"),
                 f"{80} / {5}",
                 str(i.autoclav_temp), str(i.sh))

            if self.filled:
                self.data_tables.update_row(
                    self.data_tables.row_data[c],
                    d,  # new row data
                )
            else:
                self.data_tables.add_row(
                    d
                )

    def get_task(self):
        data=f()

        print(data)
        days=g()
        self.fill_rows(data)
        self.update_days(days)


class App(MDApp):
    def build(self):
        return Container()


if __name__ == '__main__':
    App().run()
