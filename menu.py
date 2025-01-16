import flet as ft
from flet_route import Routing, path
from views import markov_page, home_page, classes_page, grade_page, triangle_page
import urls_view as urls

def main(page: ft.Page):
    page.title = "Прогноз++"
    page.theme_mode = 'dark'

    app_routes = [
        path(url=urls.home, clear=True, view=home_page.home_page),
        path(url=urls.markov_in, clear=True, view=markov_page.input_page),
        path(url=urls.markov_out, clear=True, view=markov_page.result_page),
        path(url=urls.classes_in, clear=True, view=classes_page.input_page),
        path(url=urls.classes_out, clear=True, view=classes_page.result_page),
        path(url=urls.grade_in, clear=True, view=grade_page.input_page),
        path(url=urls.grade_out, clear=True, view=grade_page.result_page),
        path(url=urls.triangle_in, clear=True, view=triangle_page.input_page),
        path(url=urls.triangle_out, clear=True, view=triangle_page.result_page),
    ]

    Routing(page=page, app_routes=app_routes)
    page.go(page.route)


ft.app(target=main)
