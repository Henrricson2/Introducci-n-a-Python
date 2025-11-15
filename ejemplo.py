#!/usr/bin/env python3
"""
Sistema Integral de Gestión de Información
Archivo: sistema_integral.py
Versión: Entrega para estudiantes

Instrucciones:
- Guarda este archivo como `sistema_integral.py`
- Ejecuta: python sistema_integral.py
"""

import random

# ------------------------------
# Helpers
# ------------------------------
def input_int(prompt, min_value=None, max_value=None):
    """Pide y valida un entero. Repite hasta recibir un entero válido."""
    while True:
        try:
            val = int(input(prompt).strip())
            if (min_value is not None) and (val < min_value):
                print(f"Ingresa un número mayor o igual a {min_value}.")
                continue
            if (max_value is not None) and (val > max_value):
                print(f"Ingresa un número menor o igual a {max_value}.")
                continue
            return val
        except ValueError:
            print("Entrada inválida. Introduce un número entero.")

def input_number(prompt):
    """Pide un número (int o float). Repite hasta recibir un número válido."""
    while True:
        s = input(prompt).strip()
        try:
            if "." in s:
                return float(s)
            else:
                return int(s)
        except ValueError:
            print("Entrada inválida. Introduce un número válido (ej: 3 o 2.5).")

# ------------------------------
# Módulos del sistema
# ------------------------------
def registrar_usuario(lista_usuarios, contadores):
    """Solicita datos del usuario y lo añade a la lista."""
    print("\n--- REGISTRO DE USUARIO ---")
    nombre = input("Nombre completo: ").strip()
    edad = input_int("Edad: ", min_value=0)
    ciudad = input("Ciudad: ").strip()
    profesion = input("Profesión: ").strip()

    usuario = {"nombre": nombre, "edad": edad, "ciudad": ciudad, "profesion": profesion}
    lista_usuarios.append(usuario)
    contadores['usuarios_registrados'] += 1

    print("✔ Usuario registrado correctamente.\n")

def procesar_texto(contadores):
    """Pide una frase y muestra análisis de texto."""
    print("\n--- PROCESAMIENTO DE TEXTO ---")
    frase = input("Escribe una frase: ")
    contadores['frases_analizadas'] += 1

    total_caracteres = len(frase)
    palabras = frase.split()
    num_palabras = len(palabras)
    mayusculas = frase.upper()
    invertida = frase[::-1]

    frecuencia = {v: 0 for v in 'aeiou'}
    for ch in frase.lower():
        if ch in frecuencia:
            frecuencia[ch] += 1

    print(f"\nTotal de caracteres: {total_caracteres}")
    print(f"Número de palabras: {num_palabras}")
    print(f"Frase en mayúsculas: {mayusculas}")
    print("Frecuencia de vocales:")
    for v, c in frecuencia.items():
        print(f"  {v}: {c}")
    print(f"Frase invertida: {invertida}\n")

def registro_numeros(contadores):
    """Solicita N números, los analiza y muestra estadísticas."""
    print("\n--- REGISTRO Y ANÁLISIS DE NÚMEROS ---")
    n = input_int("¿Cuántos números vas a ingresar? ", min_value=1)
    numeros = []
    for i in range(1, n + 1):
        num = input_number(f"Número {i}: ")
        numeros.append(num)

    contadores['listas_numericas'] += 1

    suma_total = sum(numeros)
    promedio = suma_total / len(numeros)
    mayor = max(numeros)
    menor = min(numeros)
    pares = [x for x in numeros if isinstance(x, int) and x % 2 == 0]

    print(f"\nSuma total: {suma_total}")
    print(f"Promedio: {promedio}")
    print(f"Mayor: {mayor}")
    print(f"Menor: {menor}")
    print(f"Números pares (enteros): {pares}\n")

def simulacion_aleatoria(contadores):
    """Genera 10 números aleatorios entre 1 y 100 y muestra análisis."""
    print("\n--- SIMULACIÓN ALEATORIA ---")
    lista = [random.randint(1, 100) for _ in range(10)]
    contadores['simulaciones_aleatorias'] += 1

    freq = {}
    for v in lista:
        freq[v] = freq.get(v, 0) + 1

    max_count = max(freq.values())
    mas_repetidos = [k for k, c in freq.items() if c == max_count]

    print(f"Lista generada: {lista}")
    print("Frecuencia de aparición:")
    for k in sorted(freq.keys()):
        print(f"  {k}: {freq[k]}")

    if len(mas_repetidos) == 1:
        print(f"Número más repetido: {mas_repetidos[0]} (apareció {max_count} veces)\n")
    else:
        print(f"Números más repetidos: {mas_repetidos} (cada uno apareció {max_count} veces)\n")

def mostrar_estadisticas(lista_usuarios, contadores):
    """Muestra estadísticas generales del sistema y el listado breve de usuarios."""
    print("\n--- ESTADÍSTICAS DEL SISTEMA ---")
    print(f"Usuarios registrados: {len(lista_usuarios)}")
    print(f"Frases analizadas: {contadores['frases_analizadas']}")
    print(f"Listas numéricas procesadas: {contadores['listas_numericas']}")
    print(f"Simulaciones aleatorias ejecutadas: {contadores['simulaciones_aleatorias']}\n")

    # Listado resumido de usuarios
    if lista_usuarios:
        print("Listado de usuarios registrados:")
        for i, u in enumerate(lista_usuarios, start=1):
            print(f" {i}. {u['nombre']} - {u['edad']} años - {u['ciudad']} - {u['profesion']}")
        print()
    else:
        print("No hay usuarios registrados aún.\n")

# ------------------------------
# Menú principal
# ------------------------------
def menu():
    lista_usuarios = []
    contadores = {
        'usuarios_registrados': 0,
        'frases_analizadas': 0,
        'listas_numericas': 0,
        'simulaciones_aleatorias': 0
    }

    opciones = {
        '1': ('Registrar usuario', lambda: registrar_usuario(lista_usuarios, contadores)),
        '2': ('Procesar texto', lambda: procesar_texto(contadores)),
        '3': ('Registro de números', lambda: registro_numeros(contadores)),
        '4': ('Simulación aleatoria', lambda: simulacion_aleatoria(contadores)),
        '5': ('Mostrar estadísticas', lambda: mostrar_estadisticas(lista_usuarios, contadores)),
        '6': ('Salir', None)
    }

    while True:
        print('================================================')
        print('  SISTEMA INTEGRAL DE GESTIÓN DE INFORMACIÓN  ')
        print('================================================')
        for k, (desc, _) in opciones.items():
            print(f"{k}. {desc}")
        print('------------------------------------------------')

        choice = input('Selecciona una opción: ').strip()
        if choice not in opciones:
            print('Opción inválida. Intenta de nuevo.\n')
            continue

        if choice == '6':
            print('Saliendo... ¡Hasta la próxima!')
            break

        # Ejecutar la acción
        _, action = opciones[choice]
        action()

if __name__ == '__main__':
    menu()


