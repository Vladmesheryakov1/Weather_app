import flet as ft
import os

PATH_ASSETS = os.path.abspath(__file__ + '/../assets')


class TodayWeatherContainer(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.image_column = ft.Column(
            controls=[
                ft.Container(width=100, height=100, image_src=os.path.join(PATH_ASSETS, 'weather.png'))
            ]
        )
        self.info_column = ft.Column (
            controls=[
                ft.Container(width=100, height=100, image_src=os.path.join(PATH_ASSETS, 'weather.png'))
            ]
        )

        self.controls = ft.Row(alignment=ft.alignment.center, spacing=30,
                               controls=[self.image_column, self.info_column])

    def build(self):
        return self.controls


class BlueContainer(ft.UserControl):
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
            on_click=lambda b: {},
            padding=15,
            content=ft.Column(
                alignment=ft.alignment.top_center,
                spacing=10,
                controls=[
                    ft.Row(
                        alignment=ft.alignment.center,
                        controls=[text, ft.Container(padding=ft.padding.only(bottom=5)), self.weather_container]
                    ),
                ]
            ),
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
