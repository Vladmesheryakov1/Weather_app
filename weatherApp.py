import flet as ft


class MainContainer(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.container = ft.Container(
            border_radius=35,
            bgcolor=ft.colors.BLACK,
            padding=10,
            content=ft.Column(
                width=300,
                height=550,
                controls=[
                    ft.Text("First control", color=ft.colors.WHITE),
                    ft.Text("Second control", color=ft.colors.WHITE),
                ])
        )
        self.controls = None

    def build(self):
        self.controls = [self.container]
        return self.controls


class WeatherApp:
    def __init__(self):
        self.caption = "Weather App v0.1"
        self.main_container = MainContainer()

    def run(self, page: ft.Page):
        page.add(ft.Text(self.caption), self.main_container)


ft.app(target=WeatherApp().run)
