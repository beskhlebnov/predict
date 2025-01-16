import flet as ft
import urls_view as urls
from flet_route import Params, Basket
from algorithms.triangle_module import triangle
from other import get_app_bar, get_error


def input_page(page: ft.Page, params: Params, basket: Basket):

    help_min = ft.IconButton(icon=ft.icons.HELP_OUTLINED,
                        tooltip="Min - это минимально возможный показатель по мнению эксперта")

    help_max = ft.IconButton(icon=ft.icons.HELP_OUTLINED,
                             tooltip="Max - это максимально возможный показатель по мнению эксперта")

    help_moda = ft.IconButton(icon=ft.icons.HELP_OUTLINED,
                             tooltip="Moda - это наиболее вероятный показатель по мнению эксперта")


    def minus_expert(e):
        expert_count = len(rows.controls)
        if expert_count > 4:
            rows.controls.pop(expert_count - 1)
        page.update()

    def plus_expert(e):
        rows.controls.append(
            ft.Row([
                ft.Text(f"Э{len(rows.controls) + 1}", expand=1, text_align=ft.TextAlign.CENTER),
                ft.TextField(hint_text="Введите min", expand=2),
                ft.TextField(hint_text="Введите max", expand=2),
                ft.TextField(hint_text="Введите moda", expand=2),
            ], alignment=ft.MainAxisAlignment.CENTER)
        )
        rows.scroll_to(offset=-1, duration=10)
        page.update()

    rows = ft.Column([
        ft.Row([
            ft.Text(f"Э{i + 1}", expand=1, text_align=ft.TextAlign.CENTER),
            ft.TextField(hint_text="Введите min", expand=2),
            ft.TextField(hint_text="Введите max", expand=2),
            ft.TextField(hint_text="Введите moda", expand=2),
        ], alignment=ft.MainAxisAlignment.CENTER) for i in range(4)
    ], scroll=ft.ScrollMode.ALWAYS, expand=5, alignment=ft.MainAxisAlignment.CENTER)

    def go_result(e):
        try:
            data = {"Э": [], "min": [], "max": [], "moda": []}
            for i in range(len(rows.controls)):
                min = float(rows.controls[i].controls[1].value)
                max = float(rows.controls[i].controls[2].value)
                moda = float(rows.controls[i].controls[3].value)
                if min > max:
                    get_error(page, "показатель min не может быть больше max!")
                elif moda > max:
                    get_error(page, "показатель moda не может быть больше max!")
                elif moda < min:
                    get_error(page, "показатель moda не может быть меньше min!")
                data["Э"].append(rows.controls[i].controls[0].value)
                data["min"].append(min)
                data["max"].append(max)
                data["moda"].append(moda)
            basket.data = data
            page.go(urls.triangle_out, basket=basket)
        except Exception as e:
            print(e)
            get_error(page, "Заполните все поля и повторите попытку!")

    return ft.View(urls.grade_in, controls=[
        get_app_bar(page, 5),
        ft.Row([
            ft.Text(f"Эксперт", expand=1, text_align=ft.TextAlign.CENTER),
            ft.Row([ft.Text("  Min  ", text_align=ft.TextAlign.CENTER), help_min],
                   alignment=ft.MainAxisAlignment.CENTER, expand=2),
            ft.Row([ft.Text("  Max  ", text_align=ft.TextAlign.CENTER), help_max],
                   alignment=ft.MainAxisAlignment.CENTER, expand=2),
            ft.Row([ft.Text("  Moda ", text_align=ft.TextAlign.CENTER), help_moda],
                   alignment=ft.MainAxisAlignment.CENTER, expand=2),
        ], alignment=ft.MainAxisAlignment.CENTER),
        rows,
        ft.Divider(),
        ft.Row([
            ft.IconButton(icon=ft.icons.EXPOSURE_MINUS_1, on_click=minus_expert),
            ft.IconButton(icon=ft.icons.EXPOSURE_PLUS_1, on_click=plus_expert),
        ], expand=1, alignment=ft.MainAxisAlignment.CENTER, spacing=50),
        ft.Column([ft.Row([ft.TextButton(text="Рассчитать", on_click=go_result)],
                          alignment=ft.MainAxisAlignment.CENTER)], alignment=ft.MainAxisAlignment.CENTER, expand=1)

    ])


def result_page(page: ft.Page, params: Params, basket: Basket):
    result = triangle(basket.get("data"))
    print(result)
    print(result.columns)
    return ft.View(
        urls.grade_out,
        controls=[
            get_app_bar(page, 5),
            ft.Row([
                ft.Column([
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text(f"{key}")) for key in result.columns
                        ],
                        rows=[
                            ft.DataRow(cells=[
                                ft.DataCell(ft.Text(f"{e}")) for e in v
                            ]) for v in result.values
                        ], ), ],
                    scroll=ft.ScrollMode.ALWAYS, alignment=ft.MainAxisAlignment.START, ), ],
                alignment=ft.MainAxisAlignment.CENTER, expand=1),
            ft.Column([ft.Row([ft.TextButton(text="Назад", scale=1.5, on_click=lambda _: page.go(urls.markov_in))],
                              alignment=ft.MainAxisAlignment.CENTER)], alignment=ft.MainAxisAlignment.CENTER,
                      expand=1)
        ]
    )
