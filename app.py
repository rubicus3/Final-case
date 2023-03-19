from typing import List

from kivy import Config
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable

from schemas import Day

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Window.size = (1280, 720)


class Container(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.data_tables = MDDataTable(
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(0.9, 0.6),
            use_pagination=False,
            column_data=[
                ("День/Точка", dp(30)),
                ("Оставшиеся  ресурсы", dp(40)),
                ("Расходумемые ресурсы", dp(40)),
                ("Распределение мощности реактора", dp(40)),
                ("Характеристика автоклава", dp(40)),
                ("Популяция SH", dp(40)),
            ],
            row_data=[(f"{i + 1}", "0", "0", "0", "0", "0") for i in range(1)],
        )
        self.add_widget(self.data_tables)
        self.ids["label"].text = f"Количество дней: {4}"

    def fill_rows(self, data: List[Day]):
        c = 0
        for i in data:
            c += 1
            d = [str(i.day_num), str(f"Топливо {i.remain_fuel} / Кислород {i.remain_oxi}"),
                 str(f"Топливо {i.spend_fuel} / Кислород {i.spend_fuel}"),
                 f"{i.engine_percent} / {i.electr_percent}",
                 str(i.autoclav_temp), str(i.sh)]

            self.data_tables.update_row(
                self.data_tables.row_data[c],  # old row data
                data,  # new row data
            )

    def get_task(self):
        print('afsdf')


class App(MDApp):
    def build(self):
        return Container()


if __name__ == '__main__':
    App().run()
