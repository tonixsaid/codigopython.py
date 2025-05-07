import tkinter as tk

def saludar():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    etiqueta_resultado.config(text=f"Hola {nombre}, tienes {edad} años.")

ventana = tk.Tk()
ventana.title("Mi primera app gráfica")
ventana.geometry("400x200")
ventana.config(bg="green")

etiqueta_nombre = tk.Label(ventana, text="Ingresa tu nombre:", bg="green")
etiqueta_nombre.pack()

entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

etiqueta_edad = tk.Label(ventana, text="Ingresa tu edad:", bg="green")
etiqueta_edad.pack()

entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

boton = tk.Button(ventana, text="Mostrar saludo", command=saludar)
boton.pack()

etiqueta_resultado = tk.Label(ventana, text="", bg="green")
etiqueta_resultado.pack()

etiqueta_autor = tk.Label(ventana, text="Autor: Tonix Martinez Said Emir", bg="green")
etiqueta_autor.pack(side="bottom")

ventana.mainloop()