import flet as ft


def get_view(page: ft.Page) -> ft.Column:
    num1 = ft.TextField(label="Primer número", width=200)
    num2 = ft.TextField(label="Segundo número", width=200)
    resultado = ft.Text(value="Resultado: 0", size=20)

    def Operar(e, op):
        try:
            n1 = float(num1.value)
            n2 = float(num2.value)
            if op == '+':
                r = n1 + n2
            elif op == '-':
                r = n1 - n2
            elif op == '*':
                r = n1 * n2
            else:
                r = n1 / n2 if n2 != 0 else '∞'
            resultado.value = f"Resultado: {r}"
        except ValueError:
            resultado.value = "Ingresa números válidos"
        page.update()

    def Sumar(e):
        Operar(e, '+')

    def Restar(e):
        Operar(e, '-')

    def Multiplicar(e):
        Operar(e, '*')

    def Dividir(e):
        Operar(e, '/')

    return ft.Column([
        ft.Text("Calculadora Ninja", size=30, weight=ft.FontWeight.BOLD),
        num1,
        num2,
        ft.Row([
            ft.ElevatedButton("Sumar", on_click=Sumar),
            ft.ElevatedButton("Restar", on_click=Restar),
            ft.ElevatedButton("Multiplicar", on_click=Multiplicar),
            ft.ElevatedButton("Dividir", on_click=Dividir),
        ], alignment=ft.MainAxisAlignment.CENTER),
        resultado,
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)
