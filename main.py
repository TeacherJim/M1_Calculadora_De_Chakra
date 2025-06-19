import flet as ft
from views.calculadora import get_view as Calculadora
from views.calculadora_de_rangos_ninja import get_view as CalculadoraRango


def Main(page: ft.Page):
    page.title = "Calculadora de Chakra"
    page.theme = ft.Theme(color_scheme_seed=ft.colors.ORANGE_200)
    page.bgcolor = ft.colors.ORANGE_50

    calculadora = Calculadora(page)
    rango = CalculadoraRango(page)
    contenido = ft.Container(expand=True)

    def CambiarVista(e):
        if rail.selected_index == 0:
            contenido.content = calculadora
        else:
            contenido.content = rango
        page.update()

    rail = ft.NavigationRail(
        destinations=[
            ft.NavigationRailDestination(icon=ft.icons.CALCULATE, label="Operaciones"),
            ft.NavigationRailDestination(icon=ft.icons.BOLT, label="Rango Ninja"),
        ],
        selected_index=0,
        on_change=CambiarVista,
        label_type=ft.NavigationRailLabelType.ALL,
        bgcolor=ft.colors.ORANGE_100,
    )

    CambiarVista(None)

    page.add(
        ft.Row([
            rail,
            contenido,
        ], expand=True)
    )


if __name__ == "__main__":
    ft.app(target=Main)
