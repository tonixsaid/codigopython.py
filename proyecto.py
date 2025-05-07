import tkinter as tk

def saludar():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    etiqueta_resultado.config(text=f"Hola {nombre}, tienes {edad} años.")

ventana = tk.Tk()
ventana.title("Mi primera app gráfica")  # Cambio 5
ventana.geometry("400x200")  # Cambio 1

etiqueta_nombre = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta_nombre.pack()

entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

etiqueta_edad = tk.Label(ventana, text="Ingresa tu edad:")  # Cambio 3
etiqueta_edad.pack()

entrada_edad = tk.Entry(ventana)  # Cambio 3
entrada_edad.pack()

boton = tk.Button(ventana, text="Mostrar saludo", command=saludar)  # Cambio 2
boton.pack()

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()