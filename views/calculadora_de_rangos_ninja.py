import flet as ft

RANGOS = [
    (50, "Estudiante"),
    (100, "Genin"),
    (200, "Chuunin"),
    (500, "Jounin"),
    (1000, "ANBU"),
    (float('inf'), "Kage"),
]


def get_view(page: ft.Page) -> ft.Column:
    chakra = ft.TextField(label="Puntos de chakra", width=200)
    resultado = ft.Text(value="Tu rango aparecerá aquí", size=20)

    def Calcular(e):
        try:
            valor = float(chakra.value)
            for limite, rango in RANGOS:
                if valor <= limite:
                    resultado.value = f"Eres nivel: {rango}"
                    break
        except ValueError:
            resultado.value = "Ingresa un número válido"
        page.update()

    return ft.Column([
        ft.Text("Rango Ninja", size=30, weight=ft.FontWeight.BOLD),
        chakra,
        ft.ElevatedButton("Calcular", on_click=Calcular),
        resultado,
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)
