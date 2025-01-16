import flet as ft
import urls_view as urls
from flet_route import Params, Basket
from algorithms.classes_module import classes
from other import get_app_bar, get_error


def input_page(page: ft.Page, params: Params, basket: Basket):
    standart_col = {"sm": 2}
    count_class = ft.Text(value="2")
    count_x = ft.Text(value="4")
    count_point = ft.Text(value="2")

    col_class = ft.Column([
        ft.ResponsiveRow([
            ft.TextField(hint_text="Название класса ", col=standart_col),
            ft.TextField(hint_text="X1", col=standart_col),
            ft.TextField(hint_text="X2", col=standart_col),
            ft.TextField(hint_text="X3", col=standart_col),
            ft.TextField(hint_text="X4", col=standart_col),],
            run_spacing={"xs": 10},
            alignment=ft.MainAxisAlignment.CENTER,
        ),

        ft.ResponsiveRow([
            ft.TextField(hint_text="Название класса ", col=standart_col),
            ft.TextField(hint_text="X1", col=standart_col),
            ft.TextField(hint_text="X2", col=standart_col),
            ft.TextField(hint_text="X3", col=standart_col),
            ft.TextField(hint_text="X4", col=standart_col),],
            run_spacing={"xs": 10},
            alignment=ft.MainAxisAlignment.CENTER
        ),

    ], expand=2)
    col_point = ft.Column([
        ft.ResponsiveRow([
            ft.TextField(hint_text="Название точки ", value="M1", col=standart_col),
            ft.TextField(hint_text="X1", value="1", col=standart_col),
            ft.TextField(hint_text="X2", value="3", col=standart_col),
            ft.TextField(hint_text="X3", value="2", col=standart_col),
            ft.TextField(hint_text="X4", value="1", col=standart_col),],
            run_spacing={"xs": 10},
            alignment=ft.MainAxisAlignment.CENTER,
        ),

        ft.ResponsiveRow([
            ft.TextField(hint_text="Название точки ", value="M2", col=standart_col),
            ft.TextField(hint_text="X1", value="2", col=standart_col),
            ft.TextField(hint_text="X2", value="1", col=standart_col),
            ft.TextField(hint_text="X3", value="4", col=standart_col),
            ft.TextField(hint_text="X4", value="4", col=standart_col), ],
            run_spacing={"xs": 10},
            alignment=ft.MainAxisAlignment.CENTER,
        ),

    ], expand=2)

    def minus_x(e):
        if int(count_x.value) > 3:
            count_x.value = int(count_x.value) - 1
            while int(count_x.value) < len(col_class.controls[0].controls) - 1:
                for i in range(len(col_class.controls)):
                    col_class.controls[i].controls.pop(len(col_class.controls[i].controls) - 1)
            while int(count_x.value) < len(col_point.controls[0].controls) - 1:
                for i in range(len(col_point.controls)):
                    col_point.controls[i].controls.pop(len(col_point.controls[i].controls) - 1)
            page.update()

    def plus_x(e):
        count_x.value = int(count_x.value) + 1
        while int(count_x.value) > len(col_class.controls[0].controls) - 1:
            for i in range(len(col_class.controls)):
                col_class.controls[i].controls.append(
                    ft.TextField(hint_text=f"X{len(col_class.controls[i].controls)}", col=standart_col))
        while int(count_x.value) > len(col_point.controls[0].controls) - 1:
            for i in range(len(col_point.controls)):
                col_point.controls[i].controls.append(
                    ft.TextField(hint_text=f"X{len(col_point.controls[i].controls)}", col=standart_col))
        page.update()

    def minus_class(e):
        if int(count_class.value) > 2:
            count_class.value = int(count_class.value) - 1
            while int(count_class.value) < len(col_class.controls):
                col_class.controls.pop(len(col_class.controls) - 1)
            page.update()

    def plus_class(e):
        count_class.value = int(count_class.value) + 1
        while int(count_class.value) > len(col_class.controls):
            list_control = [ft.TextField(hint_text="Название класса ", col=standart_col)]
            for i in range(int(count_x.value)):
                list_control.append(ft.TextField(hint_text=f"X{i + 1}", col=standart_col))
            col_class.controls.append(
                ft.ResponsiveRow(list_control, run_spacing={"xs": 10}, alignment=ft.MainAxisAlignment.CENTER))
        page.update()

    def minus_point(e):
        if int(count_point.value) > 1:
            count_point.value = int(count_point.value) - 1
            while int(count_point.value) < len(col_point.controls):
                col_point.controls.pop(len(col_point.controls) - 1)
            page.update()

    def plus_point(e):
        count_point.value = int(count_point.value) + 1
        while int(count_point.value) > len(col_point.controls):
            list_control = [ft.TextField(hint_text="Название точки ", col=standart_col)]
            for i in range(int(count_x.value)):
                list_control.append(ft.TextField(hint_text=f"X{i + 1}", col=standart_col))
            col_point.controls.append(
                ft.ResponsiveRow(list_control, run_spacing={"xs": 10}, alignment=ft.MainAxisAlignment.CENTER))
        page.update()

    def go_result(e):
        try:
            class_list = []
            points = []
            for i in range(len(col_class.controls)):
                if col_class.controls[i].controls[0].value == "":
                    get_error(page, f"Пропущено название класса №{i+1}!")
                    raise ValueError(f"Пропущено название класса №{i+1}!")
                else:
                    cl = {"name": col_class.controls[i].controls[0].value,
                          "centr": [int(col_class.controls[i].controls[j].value) for j in
                                    range(1, len(col_class.controls[i].controls))]}
                    class_list.append(cl)
            for i in range(len(col_point.controls)):
                if col_point.controls[i].controls[0].value == "":
                    get_error(page, f"Пропущено название точки №{i+1}!")
                    raise ValueError(f"Пропущено название точки №{i+1}!")
                else:
                    cl = {"name": col_point.controls[i].controls[0].value,
                          "centr": [int(col_point.controls[i].controls[j].value) for j in
                                    range(1, len(col_point.controls[i].controls))]}
                    points.append(cl)
            basket.classes = class_list
            basket.points = points
            page.go("/classes_result", basket=basket)
        except Exception as e:
            get_error(page, "Некоторые факторы не заполнены или заполнены не правильно, проверьте и повторите попытку!")

    return ft.View(
        urls.classes_in,
        controls=[
            get_app_bar(page, 3),
            ft.Row([
                ft.Row([ft.Text("Количество классов:"), ft.IconButton(ft.icons.EXPOSURE_MINUS_1, on_click=minus_class),
                        count_class, ft.IconButton(ft.icons.PLUS_ONE, on_click=plus_class)],
                       alignment=ft.MainAxisAlignment.START),
                ft.Row([ft.Text("Количество факторов:"), ft.IconButton(ft.icons.EXPOSURE_MINUS_1, on_click=minus_x),
                        count_x, ft.IconButton(ft.icons.PLUS_ONE, on_click=plus_x)],
                       alignment=ft.MainAxisAlignment.END),
                ft.Row([ft.Text("Количество точек:"), ft.IconButton(ft.icons.EXPOSURE_MINUS_1, on_click=minus_point),
                        count_point, ft.IconButton(ft.icons.PLUS_ONE, on_click=plus_point)],
                       alignment=ft.MainAxisAlignment.START),
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Column([
                ft.ExpansionTile(
                    controls_padding=ft.padding.only(top=15, bottom=15),
                    title=ft.Text("Классы"),
                    subtitle=ft.Text("Ввод классов для распределния"),
                    affinity=ft.TileAffinity.PLATFORM,
                    initially_expanded=True,
                    maintain_state=True,
                    collapsed_text_color=ft.colors.RED,
                    text_color=ft.colors.RED,
                    controls=[
                        ft.Column([col_class, ], scroll=ft.ScrollMode.ALWAYS, alignment=ft.MainAxisAlignment.START,
                                  expand=True)],
                    expand=2

                ),
                ft.ExpansionTile(
                    controls_padding=ft.padding.only(top=15, bottom=15),
                    title=ft.Text("Точки"),
                    subtitle=ft.Text("Ввод точек для распределния"),
                    initially_expanded=True,
                    affinity=ft.TileAffinity.PLATFORM,
                    maintain_state=True,
                    collapsed_text_color=ft.colors.BLUE,
                    text_color=ft.colors.BLUE,
                    controls=[
                        ft.Column([col_point, ], scroll=ft.ScrollMode.ALWAYS, alignment=ft.MainAxisAlignment.START,
                                  expand=True)],
                    expand=2
                ),
            ], scroll=ft.ScrollMode.ALWAYS, alignment=ft.MainAxisAlignment.START),
            ft.Column([ft.Row([ft.TextButton(text="Вычислить", scale=1.5, on_click=go_result)],
                              alignment=ft.MainAxisAlignment.CENTER)], alignment=ft.MainAxisAlignment.CENTER, expand=1)

        ])


def result_page(page: ft.Page, params: Params, basket: Basket):
    result = classes(basket.get("classes"), basket.get("points"))
    selector_current = ft.Text("1")

    point_pages = [
        ft.Column([
            ft.Row([
                ft.Container(
                    content=ft.Text(f"Оценка принадлежности точки: {i}", scale=4),
                    padding=ft.padding.only(top=20),
                ), ], alignment=ft.MainAxisAlignment.CENTER, ),
            ft.Row([ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Метод")),
                    ft.DataColumn(ft.Text("Результат")),
                ],
                rows=[
                    ft.DataRow(cells=[
                        ft.DataCell(ft.Text("Метод классификации по расстоянию до центров тяжести")),
                        ft.DataCell(ft.Text(f"{i}∈{result[i][0]}"))
                    ]),
                    ft.DataRow(cells=[
                        ft.DataCell(ft.Text("Метод классификации по скалярному произведению")),
                        ft.DataCell(ft.Text(f"{i}∈{result[i][1]}"))
                    ]),
                    ft.DataRow(cells=[
                        ft.DataCell(ft.Text("Корреляционный метод")),
                        ft.DataCell(ft.Text(f"{i}∈{result[i][2]}"))
                    ]),
                    ft.DataRow(cells=[
                        ft.DataCell(ft.Text("Метод классификации по углу между векторами и центрами тяжести классов")),
                        ft.DataCell(ft.Text(f"{i}∈{result[i][3]}"))
                    ]),
                ], ), ], alignment=ft.MainAxisAlignment.CENTER),
            ft.ExpansionTile(
                controls_padding=ft.padding.only(top=15, bottom=15),
                title=ft.Text("Вывод"),
                expanded_cross_axis_alignment=ft.CrossAxisAlignment.CENTER,
                affinity=ft.TileAffinity.PLATFORM,
                initially_expanded=True,
                maintain_state=True,
                controls=[
                    ft.Column([ft.Text(result[i][-1]), ], scroll=ft.ScrollMode.ALWAYS,
                              alignment=ft.MainAxisAlignment.CENTER, expand=True)],
                expand=2

            ),
        ], spacing=40, expand=3, alignment=ft.MainAxisAlignment.CENTER) for i in result
    ]

    selected_page = ft.Column([point_pages[0]])

    def next_point(e):
        if int(selector_current.value) < len(result):
            selector_current.value = int(selector_current.value) + 1
            selected_page.controls[0] = point_pages[int(selector_current.value) - 1]
            page.update()

    def preview_point(e):
        if int(selector_current.value) > 1:
            selector_current.value = int(selector_current.value) - 1
            selected_page.controls[0] = point_pages[int(selector_current.value) - 1]
            page.update()

    return ft.View(
        urls.classes_out,
        controls=[
            get_app_bar(page, 3),
            selected_page,
            ft.Row([
                ft.IconButton(icon=ft.icons.SKIP_PREVIOUS, on_click=preview_point),
                selector_current, ft.Text("из"), ft.Text(f"{len(result)}"),
                ft.IconButton(icon=ft.icons.SKIP_NEXT, on_click=next_point),
            ], alignment=ft.MainAxisAlignment.CENTER, expand=1),
            ft.Column([ft.Row([ft.TextButton(text="Назад", scale=1.5, on_click=lambda _: page.go(urls.classes_in))],
                              alignment=ft.MainAxisAlignment.CENTER)], alignment=ft.MainAxisAlignment.CENTER, expand=1)
        ]
    )
