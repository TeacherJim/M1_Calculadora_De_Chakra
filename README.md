
# 🧮 Calculadora de Chakra con Flet ⚡

Este proyecto está hecho con ❤️ en Python usando [Flet](https://flet.dev), una librería para crear interfaces gráficas modernas de forma sencilla y sin necesidad de conocimientos avanzados de frontend.

El objetivo es aprender **programación modular**, **estructuras básicas**, y **navegación entre vistas** mediante una app divertida basada en el mundo de Naruto 🌀.

---

## 📁 Estructura del Proyecto

```

📂 views/
├── calculadora.py              # Calculadora de operaciones simples
└── calculadora\_de\_rangos\_ninja.py # Calculadora de Rango Ninja por Chakra
main.py                           # Controlador principal con NavigationRail

````

---

## 🚀 ¿Cómo iniciar el proyecto?

Primero asegúrate de tener instalada la librería:

```bash
pip install flet==0.28.3
````

Luego corre el archivo principal:

```bash
python main.py
```

---

## 🛠️ Paso a Paso para entender el código (¡Sin copiar y pegar!)

### Paso 1: Crear la interfaz principal (`main.py`) 🧭

**¿Qué estamos haciendo?**
Imagina que estás construyendo un centro comercial 🏢. Cada vista es una tienda y el `NavigationRail` es como el mapa que te ayuda a moverte entre ellas.

**Conceptos clave:**

* `NavigationRail` → el menú de la izquierda
* `Container` → el área donde se cargan las vistas
* `page.add(...)` → agrega elementos a la pantalla principal

### Paso 2: Conectar las vistas 🧩

```python
from views.calculadora import get_view as Calculadora
from views.calculadora_de_rangos_ninja import get_view as CalculadoraRango
```

Esto es como importar "pantallas" que ya construiste para que aparezcan cuando el usuario navegue.

---

## 🧮 Vista 1: Calculadora de operaciones (`views/calculadora.py`)

### ¿Qué hace esta vista?

Permite al usuario sumar, restar, multiplicar o dividir dos números como una calculadora clásica 🧘.

### ¿Cómo se construye?

1. Usamos dos `TextField` para que el usuario escriba números.
2. Creamos 4 botones: **Sumar, Restar, Multiplicar, Dividir**.
3. Mostramos el resultado con un `Text`.

### 🧠 Analogía:

Es como una mini calculadora ninja: pides dos chakras y decides si los fusionas, los separas, los multiplicas o los divides ✨.

### 🧪 Código esencial explicado:

```python
def Operar(e, op):
    # Convierte entradas a números
    n1 = float(num1.value)
    n2 = float(num2.value)
    if op == '+':
        r = n1 + n2
```

> Usa `try/except` por si alguien intenta escribir letras en lugar de números. Así el programa no explota 💥.

---

## 🌀 Vista 2: Rango Ninja por Chakra (`views/calculadora_de_rangos_ninja.py`)

### ¿Qué hace esta vista?

Le preguntas a un estudiante su nivel de **chakra** y te responde su **rango ninja** 🥷 según una escala predefinida.

### Rangos:

* 0-50: Estudiante
* 51-100: Genin
* 101-200: Chuunin
* 201-500: Jounin
* 501-1000: ANBU
* > 1000: Kage 👑

### 🧠 Analogía:

Es como hacer un test de poder ninja: tú escribes tus puntos y te dicen si eres un aprendiz o un Hokage 💪.

### Código clave:

```python
for limite, rango in RANGOS:
    if valor <= limite:
        resultado.value = f"Eres nivel: {rango}"
```

---

## 🔄 ¿Cómo se navega entre vistas?

Cada vez que el usuario hace clic en una opción del `NavigationRail`, cambia el contenido mostrado:

```python
def CambiarVista(evento):
    if rail.selected_index == 0:
        contenido.content = calculadora
    else:
        contenido.content = rango
```

> Es como cuando cambias de pestaña en una aplicación 📱.

---

## 📚 Recomendaciones para Estudiantes

✅ **No copies y pegues todo el código.** Aprende por partes.
🧠 **Haz cambios pequeños para experimentar.** Por ejemplo, cambia colores, etiquetas o agrega nuevos botones.
💬 **Comenta tu código.** Eso te ayuda a entenderlo más tarde.
👨‍🏫 **Pregunta lo que no entiendas!** Ninguna duda es tonta.

---

## 🎓 Objetivo de aprendizaje

* Comprender estructuras básicas de Flet (TextField, Button, Text, Column, NavigationRail)
* Usar funciones en Python para separar lógica y vistas
* Crear una aplicación sencilla pero completa y funcional
