import tkinter as tk

def saludar():
    nombre = entrada.get()
    etiqueta_resultado.config(text=f"Hola {nombre}")

ventana = tk.Tk()
ventana.title("Saludo")
ventana.geometry("300x150")

etiqueta = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()
