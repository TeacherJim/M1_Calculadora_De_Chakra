import flet as ft

# Calculadora de rangos ninja basada en puntos de chakra
RANGOS = [
    (50, "Estudiante"),
    (100, "Genin"),
    (200, "Chuunin"),
    (500, "Jounin"),
    (1000, "ANBU"),
    (float('inf'), "Kage"), # Usamos float('inf') para representar cualquier valor mayor a 1000
]


# Función que retorna la vista de la calculadora de rangos ninja
def get_view(page: ft.Page) -> ft.Column: # función que recibe la página y retorna una columna con los elementos de la vista
    """Retorna la vista de la calculadora de rangos ninja."""
    chakra = ft.TextField(label="Puntos de chakra", width=200) # Campo de texto para ingresar los puntos de chakra
    resultado = ft.Text(value="Tu rango aparecerá aquí", size=20) # Texto para mostrar el resultado del rango ninja

    # Función que calcula el rango ninja basado en los puntos de chakra ingresados
    def Calcular(e):
        """Calcula el rango ninja basado en los puntos de chakra ingresados."""
        # Estructura Try-Except para manejar errores de conversión de tipo
        try:
            # Intentamos convertir el valor ingresado a float
            valor = float(chakra.value)
            # Recorremos los rangos para determinar el rango ninja correspondiente
            for limite, rango in RANGOS:
                # Si el valor ingresado es menor o igual al límite del rango
                if valor <= limite:
                    resultado.value = f"Eres nivel: {rango}" # Actualizamos el texto del resultado con el rango correspondiente
                    break
        except ValueError: # Si ocurre un error de conversión, capturamos la excepción
            resultado.value = "Ingresa un número válido"
        page.update() # Actualizamos la página para reflejar el cambio en el resultado

    # Retornamos la vista como una columna con los elementos necesarios
    return ft.Column([
        ft.Text("Rango Ninja", size=30, weight=ft.FontWeight.BOLD),
        chakra,
        ft.ElevatedButton("Calcular", on_click=Calcular),
        resultado,
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)
