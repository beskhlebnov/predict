import datetime

import flet as ft
import urls_view as urls
from flet_route import Params, Basket
from algorithms.markov_module import markov
from other import get_app_bar, get_error


def input_page(page: ft.Page, params: Params, basket: Basket):
    P_rr_text = ft.Text('Величина Pрр')
    P_rr_field = ft.TextField(width=150)

    P_pp_text = ft.Text('Величина Pпп')
    P_pp_field = ft.TextField(width=150)


    Day_text = ft.Text('Кол-во дней  ')
    Day_field = ft.TextField(width=150)

    start = {"select": "up"}

    def radiogroup_changed(e):
        start["select"] = e.control.value

    cg = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="up", label="Рост"),
            ft.Radio(value="down", label="Падение")]), on_change=radiogroup_changed)

    cg.value = "up"

    def go_result(e):
        try:
            if len(P_rr_field.value) == 0:
                get_error(page, "Величина Pрр не введена!")
            elif len(P_pp_field.value) == 0:
                get_error(page, "Величина Pпп не введена!")
            elif float(P_rr_field.value) >= 1 or float(P_rr_field.value) <= 0:
                get_error(page, "Величина Pпп введена неправильно! Значение должно находится в диапазоне от 0 до 1")
            elif float(P_pp_field.value) >= 1 or float(P_pp_field.value) <= 0:
                get_error(page, "Величина Pрр введена неправильно! Значение должно находится в диапазоне от 0 до 1")
            elif len(Day_field.value) == 0:
                get_error(page, "Введите кол-во дней!")
            elif int(Day_field.value) <= 1:
                get_error(page,"Кол-во дней должно быть больше 1")
            else:
                basket.data = {"P_pp": float(P_pp_field.value), "P_rr": float(P_rr_field.value), "start": start["select"],
                               "days": int(Day_field.value)}
                page.go(urls.markov_out, basket=basket)
        except Exception as e:
            get_error(page, "Проверь введённые данные на корректность!")

    return ft.View(
        urls.markov_in,
        controls=[
            get_app_bar(page, 2),
            ft.Column([
                ft.Row([P_rr_text, P_rr_field,
                        ft.IconButton(icon=ft.icons.HELP_OUTLINED,
                        tooltip="Ррр - это первичная вероятность роста цен, должна быть в диапазоне от 0 до 1")
                        ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([P_pp_text, P_pp_field,
                        ft.IconButton(icon=ft.icons.HELP_OUTLINED,
                        tooltip="Рпп - это первичная вероятность падения цен, должна быть в диапазоне от 0 до 1")
                        ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([Day_text, Day_field,
                        ft.IconButton(icon=ft.icons.HELP_OUTLINED,
                        tooltip="На сколько дней будет выполнен расчет, не может быть меньше 2")
                        ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([ft.Text("Первый день "), cg,
                        ft.IconButton(icon=ft.icons.HELP_OUTLINED,
                        tooltip="Что произшло в первый день исследуемого периода, падение или рост",)],
                       alignment=ft.MainAxisAlignment.CENTER),
            ], alignment=ft.MainAxisAlignment.END, expand=True),
            ft.Column(
                [ft.Row([ft.TextButton(text="Вычислить", on_click=go_result)], alignment=ft.MainAxisAlignment.CENTER)],
                alignment=ft.MainAxisAlignment.CENTER, expand=True)

        ]
    )


def result_page(page: ft.Page, params: Params, basket: Basket):
    data = basket.get("data")

    data["P_pr"] = round(1 - data["P_pp"], 3)
    data["P_rp"] = round(1 - data["P_rr"], 3)
    result = markov(data)

    return ft.View(
        urls.markov_out,
        controls=[
            get_app_bar(page, 2),
            ft.Row([
                ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("День")),
                        ft.DataColumn(ft.Text("Рр")),
                        ft.DataColumn(ft.Text("Рп"), numeric=False),
                    ],
                    rows=[
                        ft.DataRow(cells=[
                            ft.DataCell(ft.Text(result["День"][i])),
                            ft.DataCell(ft.Text(result["Рр"][i])),
                            ft.DataCell(ft.Text(result["Рп"][i])), ], ) for i in range(len(result["День"]))

                    ],
                ), ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Column([ft.Row([ft.TextButton(text="Назад", scale=1.5, on_click=lambda _: page.go(urls.markov_in))],
                              alignment=ft.MainAxisAlignment.CENTER)], alignment=ft.MainAxisAlignment.CENTER, expand=1)
        ]
    )
