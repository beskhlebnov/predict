import flet as ft
import urls_view as urls


def get_app_bar(page, selected):
    return ft.AppBar(
        leading_width=100,
        title=ft.Row([
            ft.Image(src=f"sample/logo.png", width=50),
            ft.Text("Прогноз++")]),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.TextButton("Главная", disabled=selected == 1, on_click=lambda _: page.go(urls.home)),
            ft.TextButton("Цепи маркова", disabled=selected == 2, on_click=lambda _: page.go(urls.markov_in)),
            ft.TextButton("Автоматическая классификация", disabled=selected == 3,
                          on_click=lambda _: page.go(urls.classes_in)),
            ft.TextButton("Скользящая средняя", disabled=selected == 4, on_click=lambda _: page.go(urls.grade_in)),
            ft.TextButton("Треугольное распределение", disabled=selected == 5, on_click=lambda _: page.go(urls.triangle_in)),
            ft.IconButton(icon=ft.icons.EXIT_TO_APP, icon_color=ft.colors.BLUE, on_click=lambda _: page.window_close()),
        ],
    )


def get_error(page, error):
    page.snack_bar = ft.SnackBar(ft.Text(error))
    page.snack_bar.open = True
    page.update()
