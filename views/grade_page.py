import flet as ft
import matplotlib
import matplotlib.pyplot as plt
import io
import base64
import urls_view as urls
from flet_route import Params, Basket
from algorithms.grade_module import grade
from other import get_app_bar, get_error
matplotlib.use("svg")

def input_page(page: ft.Page, params: Params, basket: Basket):

    def minus_day(e):
        day_count = len(rows.controls)
        if day_count > 10:
            rows.controls.pop(day_count - 1)
        page.update()

    def plus_day(e):
        rows.controls.append(
            ft.Row([
                ft.Text(f"День {len(rows.controls) + 1}"),
                ft.TextField(hint_text="Введите значение")
            ], alignment=ft.MainAxisAlignment.CENTER)
        )
        rows.scroll_to(offset=-1, duration=10)
        page.update()

    rows = ft.Column([
        ft.Row([
            ft.Text(f"День {i+1}"),
            ft.TextField(hint_text="Введите значение", value=f"{50+(i%2)}")
        ], alignment=ft.MainAxisAlignment.CENTER) for i in range(15)
    ], scroll=ft.ScrollMode.ALWAYS, expand=5, alignment=ft.MainAxisAlignment.CENTER)

    def go_result(e):
        try:
            basket.data = {"День": [rows.controls[i].controls[0].value for i in range(len(rows.controls))], "Значение": [float(rows.controls[i].controls[1].value) for i in range(len(rows.controls))]}
            page.go(urls.grade_out, basket=basket)
        except Exception as e:
            get_error(page, "Заполните все поля и повторите попытку!")

    return ft.View(urls.grade_in, controls=[
            get_app_bar(page, 4),
            rows,
            ft.Divider(),
            ft.Row([
                ft.IconButton(icon=ft.icons.EXPOSURE_MINUS_1, on_click=minus_day),
                ft.IconButton(icon=ft.icons.EXPOSURE_PLUS_1, on_click=plus_day),
            ], expand=1, alignment=ft.MainAxisAlignment.CENTER, spacing=50),
            ft.Column([ft.Row([ft.TextButton(text="Рассчитать", on_click=go_result)], alignment=ft.MainAxisAlignment.CENTER)],alignment=ft.MainAxisAlignment.CENTER, expand=1)

        ])


def result_page(page: ft.Page, params: Params, basket: Basket):
    result = grade(basket.get("data"))
    plt.figure(figsize=(10, 6))
    result.plot(x="День", y=["Cредняя (3)", "Cредняя (5)"])
    plt.xlabel("Дни")
    plt.ylabel("Значения")
    plt.title("Скользящая средняя")

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    chart_data = base64.b64encode(buf.read()).decode('utf-8')

    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    ax.table(cellText=result.values, colLabels=result.columns, loc='center')
    fig.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    image_data = base64.b64encode(buf.read()).decode('utf-8')

    return ft.View(
            urls.grade_out,
            controls=[
                get_app_bar(page, 4),
                ft.Row([
                ft.Row([ft.Column([ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text(f"{key}")) for key in result.columns
                        ],
                        rows=[
                            ft.DataRow(cells=[
                                ft.DataCell(ft.Text(f"{e}")) for e in v
                            ]) for v in result.values
                        ], ),], scroll=ft.ScrollMode.ALWAYS, alignment=ft.MainAxisAlignment.START,),], alignment=ft.MainAxisAlignment.CENTER, expand=1),
                ft.Row([
                    ft.Image(
                        src_base64=chart_data,
                        expand=True,
                    ),
                ], alignment=ft.MainAxisAlignment.CENTER, expand=1),
                ], expand=2),
                ft.Column([ft.Row([ft.TextButton(text="Назад", scale=1.5, on_click=lambda _: page.go(urls.markov_in))],
                                  alignment=ft.MainAxisAlignment.CENTER)], alignment=ft.MainAxisAlignment.CENTER,
                          expand=1)
            ]
        )