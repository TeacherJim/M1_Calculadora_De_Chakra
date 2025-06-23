import flet as ft

# Calculadora simple que permite realizar operaciones básicas
def get_view(page: ft.Page) -> ft.Column:
    """Retorna la vista de la calculadora simple."""
    # Definición de los campos de entrada y el resultado
    num1 = ft.TextField(label="Primer número", width=200)
    num2 = ft.TextField(label="Segundo número", width=200)
    resultado = ft.Text(value="Resultado: 0", size=20)

    # Funciones para realizar las operaciones matemáticas
    def Operar(e, op):
        """Realiza la operación matemática seleccionada."""
        #Estructura Try-Except para manejar errores de conversión de tipo
        try:
            # Intentamos convertir los valores ingresados a float
            n1 = float(num1.value)
            n2 = float(num2.value)
            # Dependiendo de la operación seleccionada, realizamos el cálculo
            if op == '+': # Suma
                r = n1 + n2
            elif op == '-': # Resta
                r = n1 - n2
            elif op == '*': # Multiplicación
                r = n1 * n2
            else:
                r = n1 / n2 if n2 != 0 else '∞'# División, manejando la división por cero
            resultado.value = f"Resultado: {r}"
        except ValueError: # Si ocurre un error de conversión, capturamos la excepción
            resultado.value = "Ingresa números válidos"
        page.update()

    def Sumar(e): # Realiza la suma
        Operar(e, '+')

    def Restar(e): # Realiza la resta
        Operar(e, '-')

    def Multiplicar(e): # Realiza la multiplicación
        Operar(e, '*')

    def Dividir(e): # Realiza la división
        Operar(e, '/')

    return ft.Column([
        # Título de la calculadora
        ft.Text("Calculadora Ninja", size=30, weight=ft.FontWeight.BOLD),
        num1, # Primer campo de entrada para el primer número
        num2,# Segundo campo de entrada para el segundo número
        ft.Row([
            # Botones para realizar las operaciones
            ft.ElevatedButton("Sumar", on_click=Sumar),
            ft.ElevatedButton("Restar", on_click=Restar),
            ft.ElevatedButton("Multiplicar", on_click=Multiplicar),
            ft.ElevatedButton("Dividir", on_click=Dividir),
        ], alignment=ft.MainAxisAlignment.CENTER),
        resultado, # Texto para mostrar el resultado de la operación
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)
