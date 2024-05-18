import flet
from flet import Animation
from flet import *
import requests
import datetime
import geocoder
import os
import threading


class State:
    i = 0


s = State()
sem = threading.Semaphore()

PATH_ASSETS = os.path.abspath(__file__ + '/../assets')  # решение проблемы отображения картинок

lat = 0
lon = 0
result_get_info = None


def get_coordinates():
    global lat, lon
    location = geocoder.ip('me')

    if location.ok:
        latitude, longitude = location.latlng  # получаем данные
        lat = latitude
        lon = longitude  # закидываем в глобальную переменную
        print(f"Ваши координаты: Широта {latitude}, Долгота {longitude}")
    else:
        print("Не удалось определить ваши координаты.")


def get_info():
    global lat, lon, result_get_info
    API = 'da2fa4dd5cb56e0a80fee9e43ddd0d58'
    URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API}&units=metric'
    result_get_info = requests.get(URL).json()
    print(result_get_info)
    temp = result_get_info['main']['temp']
    return result_get_info


class Blue_Container:
    def __init__(self, result_get_info):
        self.result_get_info = result_get_info

    def create_container(self):
        universal_container = Container(
            width=310,
            height=660 * 0.40,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=["lightblue600", "lightblue900"],
            ),
            border_radius=35,
            animate=animation.Animation(duration=350, curve=AnimationCurve.DECELERATE, ),
            on_click=lambda b: _expand(b),
            padding=15,
            content=Column(
                alignment=alignment.top_center,
                spacing=10,
                controls=[
                    Row(
                        alignment=alignment.center,
                        controls=[
                            Text(
                                #отображаемая информация ',
                                size=16,
                            )
                        ],
                    ),
                ]
            ),
        )
        return universal_container

    # def _expand(e):
    #     '''animation'''
    #     pass


blue_container = Blue_Container.create_container(result_get_info)


def main(page: Page):
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER

    get_coordinates()
    '''получаем координаты'''
    get_info()
    '''получаем данные с openweather'''

    def _expand(e):
        if _c.content.controls[0].height == 560:
            _c.content.controls[0].height = 660 * 0.40
            _c.content.controls[0].update()
        else:
            _c.content.controls[0].height = 560
            _c.content.controls[0].update()

    def _top():

        top = Container(
            width=310,
            height=660 * 0.40,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=["lightblue600", "lightblue900"],
            ),
            border_radius=35,
            animate=animation.Animation(duration=350, curve=AnimationCurve.DECELERATE, ),
            on_click=lambda e: _expand(e),
            padding=15,
            content=Column(
                alignment=alignment.top_center,
                spacing=10,
                controls=[
                    Row(
                        alignment=alignment.center,
                        controls=[
                            Text(
                                f'{result_get_info['name']}, {result_get_info['sys']['country']}',
                                size=16,
                            )
                        ],
                    ),
                    Container(padding=padding.only(bottom=5)),
                    Row(
                        alignment=alignment.center,
                        spacing=30,
                        controls=[
                            Column(
                                controls=[
                                    Container(
                                        width=100,
                                        height=100,
                                        image_src=os.path.join(PATH_ASSETS, 'weather.png'),
                                    )
                                ]
                            ),
                            Column(
                                spacing=5,
                                horizontal_alignment=alignment.center,
                                controls=[
                                    Text(
                                        "Today",
                                        size=12,
                                        text_align=alignment.center,
                                    ),
                                    Row(
                                        vertical_alignment=alignment.center,
                                        spacing=0,
                                        controls=[
                                            Container(
                                                content=Text(f'{result_get_info['main']['temp']} C° ',
                                                             size=20, text_align=alignment.center
                                                             ),
                                            )
                                        ],
                                    ),
                                    Row(
                                        vertical_alignment=alignment.center,
                                        controls=[
                                            Container(
                                                content=Text(f'{result_get_info['weather'][0]['main']} - '
                                                             f'{result_get_info['weather'][0]['description']}',
                                                             size=10,
                                                             text_align=alignment.center,
                                                             color="white54"
                                                             ),
                                            )
                                        ]
                                    )
                                ]
                            )
                        ]
                    ),
                    Divider(height=8, thickness=2, color="white10"),
                    Row(
                        alignment="spaceEvenly",
                        controls=[
                            Container(
                                content=Column(
                                    horizontal_alignment="center",
                                    spacing=2,
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            content=Image(src=os.path.join(PATH_ASSETS, 'wind.png'),
                                                          color="white", ),
                                            width=20,
                                            height=20,
                                        ),
                                        Text(
                                            f'{result_get_info['wind']['speed']} m/s',
                                            size=10, text_align=alignment.center,
                                        ),
                                        Text(
                                            'Wind', size=10, text_align=alignment.center,
                                            color="white54"
                                        ),
                                    ]
                                ),
                            ),
                            Container(
                                content=Column(
                                    horizontal_alignment="center",
                                    spacing=2,
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            content=Image(src=os.path.join(PATH_ASSETS, 'wind.png'),
                                                          color="white", ),
                                            width=20,
                                            height=20,
                                        ),
                                        Text(f'{result_get_info['main']['humidity']} % ',
                                             size=10, text_align=alignment.center),
                                        Text('Humidity', size=10, text_align=alignment.center,
                                             color="white54"),
                                    ]
                                ),
                            ),
                            Container(
                                content=Column(
                                    horizontal_alignment="center",
                                    spacing=2,
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            content=Image(src=os.path.join(PATH_ASSETS, 'wind.png'),
                                                          color="white", ),
                                            width=20,
                                            height=20,
                                        ),
                                        Text(f'{result_get_info['main']['feels_like']}° ',
                                             size=10, text_align=alignment.center),
                                        Text('feels_like', size=10, text_align=alignment.center,
                                             color="white54"),
                                    ]
                                ),
                            ),
                        ],
                    ),
                    Row(),
                    Row(
                        alignment="spaceEvenly",
                        controls=[
                            Container(

                                bgcolor="white10",
                                border_radius=12,
                                alignment=alignment.center,
                                width=110,
                                height=110,
                            ),
                            Container(

                                bgcolor="white10",
                                border_radius=12,
                                alignment=alignment.center,
                                width=110,
                                height=110,
                            ),
                        ]
                    ),
                    Row(
                        alignment="spaceEvenly",
                        controls=[
                            Container(

                                bgcolor="white10",
                                border_radius=12,
                                alignment=alignment.center,
                                width=110,
                                height=110,
                            ),
                            Container(

                                bgcolor="white10",
                                border_radius=12,
                                alignment=alignment.center,
                                width=110,
                                height=110,
                            ),
                        ]
                    ),
                ],
            ),
        )
        return top

    def on_scroll(e: flet.OnScrollEvent):
        if e.pixels >= e.max_scroll_extent - 100:
            if sem.acquire(blocking=False):
                try:
                    for _top in _c:
                        _c.update()
                finally:
                    sem.release()

    _c = Container(
        # width=None,
        # height=None,
        border_radius=35,
        bgcolor='black',
        padding=10,
        content=Column(
            width=300,
            height=550,
            scroll=flet.ScrollMode.ALWAYS,
            on_scroll_interval=0,
            on_scroll=on_scroll,
            controls=[_top(), blue_container]),
    )

    page.add(_c)
    page.update()


if __name__ == "__main__":
    flet.app(target=main, assets_dir="assets")
