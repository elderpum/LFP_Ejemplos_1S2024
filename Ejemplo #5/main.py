# Librería a utilizar
# Instalamos Tkinter para poder utilizar la interfaz gráfica
# pip install tk

# Importamos la librería de Tkinter
from tkinter import *
from tkinter import ttk

def segundaVentana():
    # Creamos una nueva ventana
    color = '#FF9115'
    root = Tk()
    # Hacemos una ventana grande 600x400
    frm = ttk.Frame(root, width=600, height=400)
    frm.grid()
    ttk.Label(frm, text="Nombre: Elder Pum").grid(column=0, row=0)
    ttk.Label(frm, text="Carnet: 201700761").grid(column=0, row=1)
    ttk.Label(frm, text="Curso: Lenguajes Formales y de Programación").grid(column=0, row=2)
    ttk.Button(frm, text="Regresar", command=root.destroy).grid(column=0, row=3)
    root.mainloop()

def terceraVentana():
    # Creamos una tercena ventana con un text area para ingresar texto
    root = Tk()
    # Le cambiamos el nombre a la ventana
    root.title("Compilador")
    # Hacemos una ventana grande 400x800
    frm = ttk.Frame(root, width=1000, height=1200)
    frm.grid()
    # Creamos un text area
    textAreaInicial = Text(frm, width=50, height=25)
    textAreaInicial.grid(column=1, row=1)
    # Creamos un botón para obtener la data de un archivo
    ttk.Button(frm, text="Obtener Data", command=obtenerTexto(textAreaInicial)).grid(column=3, row=0)
    # Creamos un botón para obtener el texto
    ttk.Button(frm, text="Compilar", command=obtenerTexto(textAreaInicial)).grid(column=3, row=1)
    # Creamos un botón para regresar
    ttk.Button(frm, text="Regresar", command=root.destroy).grid(column=3, row=3)

    textAreaFinal = Text(frm, width=50, height=25)
    textAreaFinal.grid(column=5, row=1)
    root.mainloop()

def obtenerTexto(textArea):
    # Obtenemos linea por linea el texto ingresado y lo guardamos en un array
    texto = textArea.get("1.0", "end").split("\n")
    print(texto)

def main():
    # Creamos un hola mundo simple
    root = Tk()
    # Hacemos una ventana grande 600x400
    frm = ttk.Frame(root, width=600, height=400)
    frm.grid()
    ttk.Label(frm, text="Hola, mundo!").grid(column=0, row=0)
    ttk.Button(frm, text="Salir", command=root.destroy).grid(column=0, row=1)
    ttk.Button(frm, text="Abrir Datos Personales", command=segundaVentana).grid(column=0, row=2)
    ttk.Button(frm, text="Abrir Text Area", command=terceraVentana).grid(column=0, row=3)
    root.mainloop()

main()