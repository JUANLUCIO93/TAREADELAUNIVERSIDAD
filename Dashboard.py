import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'UNIDAD 1/Semana 2/Tecnicas de Programacion/Ejemplo Tecnicas de Programacion.py',
        '2': 'UNIDAD 1/Semana 3/situaciones del mundo real/Ejemplos del Mundo Real.py',
        '3': 'UNIDAD 1/Semana 4/el promedio semanal del clima/Programación Orientada a Objetos Programación Tradicional.py',
        '4': 'UNIDAD 2/Semana 5/Desarrollo de un pequeño programa/Tipos de datos.py',
        '5': 'UNIDAD 2/Semana 6/Aplicacion de Conceptos de POO/definicion_de_clase_herencia_encapsulacion.py',
        '6': 'UNIDAD 2/Semana 7/Constructores_y_Destructores/concepto_sobre_constructores_y_destructores.py',

    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()