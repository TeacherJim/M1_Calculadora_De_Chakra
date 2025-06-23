import flet as ft
# Importando las vistas
from views.calculadora import get_view as Calculadora
from views.calculadora_de_rangos_ninja import get_view as CalculadoraRango

# Flet app para la integración del NavigationRail y las vistas
def Main(page: ft.Page):
    # Configuración de la página
    page.title = "Calculadora de Chakra"
    # Establecer el tema y el color de fondo
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.ORANGE_200)
    page.bgcolor = ft.Colors.ORANGE_50

    # Configuración del NavigationRail y las vistas
    calculadora = Calculadora(page) # Vista de la calculadora
    rango = CalculadoraRango(page) # Vista de rango ninja
    contenido = ft.Container(expand=True) # Contenedor para el contenido de las vistas

    # Función para cambiar la vista según la selección del NavigationRail
    def CambiarVista(e):
        """Cambia el contenido del contenedor según la vista seleccionada."""

        if rail.selected_index == 0: # Si la opción seleccionada es "Operaciones"
            contenido.content = calculadora
        else: # de otro modo, si es "Rango Ninja"
            contenido.content = rango
        page.update() # Actualiza la página para reflejar el cambio

    # Configuración del NavigationRail
    rail = ft.NavigationRail(
        destinations=[
            # Definición de las opciones del NavigationRail
            ft.NavigationRailDestination(icon=ft.Icons.CALCULATE, label="Operaciones"),
            # Definición de la opción de rango ninja
            ft.NavigationRailDestination(icon=ft.Icons.BOLT, label="Rango Ninja"),
        ],
        selected_index=0, # Índice seleccionado por defecto
        on_change=CambiarVista, # Evento que se dispara al cambiar la selección
        label_type=ft.NavigationRailLabelType.ALL, # Mostrar etiquetas de todas las opciones
        bgcolor=ft.Colors.ORANGE_100, # Color de fondo del NavigationRail
    )

    CambiarVista(None) # Inicializar la vista con la calculadora
    # Añadir el NavigationRail y el contenedor de contenido a la página
    page.add(
        ft.Row([
            rail,
            contenido,
        ], expand=True)
    )

#Si el script se ejecuta directamente, inicia la aplicación Flet
if __name__ == "__main__":
    ft.app(target=Main)
