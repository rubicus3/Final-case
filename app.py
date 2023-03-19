from kivy import Config
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Window.size = (1280, 720)




class Table(MDDataTable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Container(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # self.data_tables = MDDataTable(
        #     pos_hint={"center_y": 0.5, "center_x": 0.5},
        #     size_hint=(0.8, 0.6),
        #     use_pagination=False,
        #     column_data=[
        #         ("No. 1"),
        #         ("Оставшиеся ресурсы"),
        #         ("Расходуемые ресурсы"),
        #         ("Распределение мощности реактора"),
        #         ("Характеристика автоклава"),
        #         ("Популяция SH"),
        #     ],
        #     row_data=[
        #         (''),
        #         (''),
        #         (''),
        #         (''),
        #         (''),
        #     ],
        # )

        self.data_tables = MDDataTable(
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(0.9, 0.6),
            use_pagination=False,
            column_data=[
                ("No.", dp(30)),
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


class App(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "BlueGray"
        return Container()


if __name__ == '__main__':
    App().run()