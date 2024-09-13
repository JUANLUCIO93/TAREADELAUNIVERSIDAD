import tkinter as tk
from tkinter import messagebox

# Función para agregar la información a la lista
def agregar_info():
    info = entrada.get()
    if info:
        lista.insert(tk.END, info)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, introduce la información valida.")

# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz gráfica de usuario (GUI)")
ventana.geometry("500x500")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Ingrese el valor:")
etiqueta.pack(pady=20)

# Crear un campo de texto
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)

# Crear un botón para agregar información
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_info, bg="green", fg="yellow")
boton_agregar.pack(pady=5)

# Crear un botón para limpiar la lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista, bg="yellow", fg="blue")
boton_limpiar.pack(pady=5)

# Crear una lista con fondo blaco, bordes rosados y texto azul
lista = tk.Listbox(ventana, height=10, width=40, bg="white", fg="blue", highlightbackground="pink", highlightthickness=3)
lista.pack(pady=10)

# Ejecutar el bucle principal de eventos
ventana.mainloop()
