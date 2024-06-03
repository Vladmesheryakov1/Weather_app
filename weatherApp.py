import flet as ft
import os


class AssetsHelper:
    def __init__(self, path: str = None):
        file_dir = os.path.dirname(__file__)
        self.assetsPath = os.path.abspath(file_dir + path)

    def getFilePath(self, filename: str):
        return os.path.join(self.assetsPath, filename)


assets = AssetsHelper('/assets')


class TodayWeatherContainer(ft.UserControl):
    def __init__(self):
        super().__init__()
        img_src = assets.getFilePath('weather.png')
        self.image_column = ft.Column(
            controls=[
                ft.Container(width=100, height=100, image_src=img_src)
            ]
        )

        self.today_desc = ft.Text(size=12, text_align=ft.alignment.center, value='Today')

        self.temp_val = ft.Row(vertical_alignment=ft.alignment.center, spacing=0, controls=[
            ft.Text("17.93 C", size=20, text_align=ft.alignment.center)
        ])

        self.weather_desc = ft.Row(vertical_alignment=ft.alignment.center, controls=[
            ft.Text("Clouds - broken clouds", size=10, text_align=ft.alignment.center, color=ft.colors.WHITE54)
        ])

        self.info_column = ft.Column (
            spacing=5,
            horizontal_alignment=ft.alignment.center,
            controls=[self.today_desc, self.temp_val, self.weather_desc]
        )

        padding = ft.Container(padding=ft.padding.only(bottom=5))
        self.controls = ft.Row(alignment=ft.alignment.center, spacing=30,
                               controls=[self.image_column, padding, self.info_column])

    def build(self):
        return self.controls


class BlueContainer(ft.UserControl):

    def resize(self, e):
        if self.container.height == 560:
            self.container.height = 660 * 0.40
            self.container.update()
        else:
            self.container.height = 560
            self.container.update()

    def __init__(self, text: ft.Text):
        super().__init__()
        self.weather_container = TodayWeatherContainer()
        self.container = ft.Container(
            width=310,
            height=660 * 0.40,
            gradient=ft.LinearGradient(
                begin=ft.alignment.bottom_left,
                end=ft.alignment.top_right,
                colors=[ft.colors.LIGHT_BLUE_600, ft.colors.LIGHT_BLUE_900],
            ),
            border_radius=35,
            animate=ft.animation.Animation(duration=350, curve=ft.AnimationCurve.DECELERATE, ),
            on_click=lambda e: self.resize(e),
            padding=15,
            content=ft.Column(
                alignment=ft.alignment.top_center,
                spacing=10,
                controls=[
                    ft.Row(alignment=ft.alignment.center, controls=[text]),
                    ft.Container(padding=ft.padding.only(bottom=5)),
                    ft.Row(alignment=ft.alignment.center, controls=[self.weather_container])
                ]
            )
        )

    def build(self):
        self.controls = [self.container]
        return self.controls


class MainContainer(ft.UserControl):
    def __init__(self, controls):
        super().__init__()
        self.container = ft.Container(
            border_radius=35,
            bgcolor=ft.colors.BLACK,
            padding=10,
            content=ft.Column(
                width=300,
                height=550,
                controls=controls
            )
        )
        self.controls = None

    def build(self):
        self.controls = [self.container]
        return self.controls


class WeatherApp:
    def __init__(self):
        self.caption = "Weather App v0.1"
        self.blue_container = BlueContainer(ft.Text("Blue container parameter text", size=16))
        self.secondary_blue_container = BlueContainer(ft.Text("Secondary Blue container parameter text", size=22))
        self.main_container = MainContainer([self.blue_container, self.secondary_blue_container])

    def run(self, page: ft.Page):
        page.add(ft.Text(self.caption), self.main_container)


ft.app(target=WeatherApp().run)
