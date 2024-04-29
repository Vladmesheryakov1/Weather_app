import flet
from flet import Animation
from flet import *
import requests
import datetime
import geocoder
import os  # решение проблемы отображения картинок

PATH_ASSETS = os.path.abspath(__file__ + '/../assets') # решение проблемы отображения картинок

lat = 0
lon = 0
result_get_info = None

days = [
    "Mon",
    "Tue",
    "Wed",
    "Thu",
    "Fri",
    "Sat",
    "Sun",
]


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


# top container

def main(page: Page):
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER

    get_coordinates()
    '''получаем координаты'''
    get_info()
    '''получаем данные с openweather'''

    def _middle():

        middle = Container(
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
                ]
            ),
        )
        return middle

    def _expand(e):
        if _c.content.controls[0].height == 560:
            _c.content.controls[0].height = 660 * 0.40
            _c.content.controls[0].update()
        else:
            _c.content.controls[0].height = 560
            _c.content.controls[0].update()

    def _top():

        # _today = current_temp()

        _today_extra = GridView(
            max_extent=150,
            expand=1,
            run_spacing=5,
            spacing=5,

        )

        for info in get_info():
            _today_extra.controls.append(info)

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
            on_hover=lambda e: _expand(e),
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

    _c = Container(
        width=310,
        height=660,
        border_radius=35,
        bgcolor='black',
        padding=10,
        content=Column(width=300, height=550, controls=[_top(), _middle()]),
    )
    page.add(_c)
    page.update()


if __name__ == "__main__":
    flet.app(target=main, assets_dir="assets")
