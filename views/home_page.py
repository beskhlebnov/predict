import flet as ft
from flet_route import Params, Basket
import urls_view as urls
from other import get_app_bar


def home_page(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        urls.home,
        controls=[
            get_app_bar(page, 1),
            ft.Text("Добро пожаловать в Прогноз++, здесь вы сможете без труда использовать многие экспертные методы для анализа рынка и пронозирования цен",
                    size=25),
            ft.Text("Для навигации между методами используйте верхнюю панель",
                    size=25)
        ]
    )
