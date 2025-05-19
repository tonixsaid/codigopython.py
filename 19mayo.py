import tkinter as tk
from tkinter import ttk, messagebox
# vventana default
def area_dinamica_limpia():
    """Limpia todos los widgets del área dinámica antes de cargar nuevos."""
    for widget in area_dinamica.winfo_children():
        widget.destroy()

def inicio_bienvenida():
    """Muestra un mensaje de bienvenida en el área dinámica."""
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Hola y bienvenido", font=("Arial", 14)).pack(pady=10)
    tk.Button(area_dinamica, text="Mostrar bienvenida", command=lambda: messagebox.showinfo("Título", "Mensaje temporal")).pack()

# Lista de datos
datos_guardados_lista = []

def interfaz_datos():
    """Interfaz para ingresar y visualizar múltiples datos de alumnos."""
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Ingreso de datos", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Ingresa tu nombre:").pack()
    campo_texto_uno = tk.Entry(area_dinamica)
    campo_texto_uno.pack(pady=5)

    tk.Label(area_dinamica, text="Selección A:").pack()
    opcion_elegida = tk.StringVar(value="Opción 1")
    tk.Radiobutton(area_dinamica, text="Opción 1", variable=opcion_elegida, value="Opción 1").pack()
    tk.Radiobutton(area_dinamica, text="Opción 2", variable=opcion_elegida, value="Opción 2").pack()

    tk.Label(area_dinamica, text="Lista desplegable:").pack()
    combo = ttk.Combobox(area_dinamica, values=["Uno", "Dos", "Tres"])
    combo.pack()
    combo.current(0)

    # datos almacenados
    lista_datos_mostrados = tk.Label(area_dinamica, text="", justify="left", fg="black", font=("Arial", 11))
    lista_datos_mostrados.pack(pady=10)

    def accion_guardar():
        """Guarda y muestra los datos ingresados en lista."""
        nombre = campo_texto_uno.get()
        seleccion = opcion_elegida.get()
        opcion_lista = combo.get()

        if nombre:  # no guarden entradas vacías
            datos_guardados_lista.append(f"Nombre: {nombre}, Selección: {seleccion}, Lista: {opcion_lista}")
            lista_datos_mostrados.config(text="\n".join(datos_guardados_lista))

    tk.Button(area_dinamica, text="Guardar datos", command=accion_guardar).pack(pady=10)

def interfaz_color():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Configuraciones de color", font=("Arial", 14)).pack(pady=10)

    colores = ["lightblue", "lightgreen", "lightyellow", "lightgray"]
    tk.Label(area_dinamica, text="Cambiar fondo:").pack()

    def cambiar_color(c):
        ventana_principal.config(bg=c)
        menu_lateral.config(bg=c)
        area_dinamica.config(bg=c)

    for c in colores:
        tk.Button(area_dinamica, text=c, bg=c, width=20, command=lambda col=c: cambiar_color(col)).pack(pady=2)

def interfaz_preguntas():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="El alumno deberia mejorar su rendimiento", font=("Arial", 14)).pack(pady=10)
    contenido = (
        "Explica con tus palabras:\n\n"
        "- ¿Qué hace cada botón?\n"
        "- ¿Qué cambias si modificas un texto?\n"
        "- ¿Cómo cambias un color?\n"
        "- ¿Qué debes renombrar?"
    )
    tk.Label(area_dinamica, text=contenido, justify="left").pack(pady=10)

# ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Interfaz de prácticas")
ventana_principal.geometry("600x600")
ventana_principal.config(bg="lightblue")

# Creación de vnetnanas
menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=150)
menu_lateral.pack(side="left", fill="y")

area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")

# Botones demenu
tk.Button(menu_lateral, text="Inicio", command=inicio_bienvenida, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Ingreso de datos", command=interfaz_datos, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Configuración", command=interfaz_color, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Ayuda", command=interfaz_preguntas, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Salir", command=ventana_principal.destroy, width=15).pack(pady=30)

inicio_bienvenida()
ventana_principal.mainloop()
