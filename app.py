from kivy import Config
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel

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
            row_data=[(f"{i + 1}", "1", "2", "3", "4", "5") for i in range(3)],
        )
        self.add_widget(self.data_tables)
        self.ids["label"].text = f"Количество дней: {4}"

    def update_row(self, data=["1","1","1","1","1",]):
        self.data_tables.update_row(
            self.data_tables.row_data[1],  # old row data
            data,  # new row data
        )


    def update_days(self):
        pass

class App(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "BlueGray"
        return Container()


if __name__ == '__main__':
    App().run()