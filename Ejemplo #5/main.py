# Librería a utilizar
# Instalamos Tkinter para poder utilizar la interfaz gráfica
# pip install tk

# Importamos la librería de Tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class Lexema:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

class Error:
    def __init__(self, mensaje):
        self.mensaje = mensaje
        
def analizadorLexico(textAreaInicial, textAreaFinal):
    lexemas = []
    errores = []
    palabra = ""
    # Obtenemos el texto del text area
    texto = textAreaInicial.get("1.0", "end")
    
    # Iteramos sobre cada caracter del texto
    i = 0
    while i < len(texto):
        char = texto[i]

        # Verificamos que el caracter sea una letra o un dígito
        if char.isalnum():
            # Iteramos los caracteres para obtener la palabra completa
            while i < len(texto) and texto[i].isalnum():
                palabra += texto[i]
                i += 1

            # Verificar si la palabra es una palabra reservada
            if palabra.lower() in ['doctype', 'html', 'head', 'title', 'body', 'h1', 'p', 'h2']:
                lexemas.append(Lexema("PALABRA_RESERVADA", palabra.lower()))
            elif palabra.isdigit():
                lexemas.append(Lexema("NUMERO", palabra))
            else:
                lexemas.append(Lexema("PALABRA", palabra))
            palabra = ""

        # Verificamos otros caracteres especiales
        elif char in [',']:
            lexemas.append(Lexema("COMA", char))
        elif char in ['.']:
            lexemas.append(Lexema("PUNTO", char))
        elif char in ['+', '-', '*', '/', '<', '>', '!']:
            lexemas.append(Lexema("ESPECIAL", char))
        # Ignoramos estos caracteres
        elif char in [' ', '\n', '\t', '\r']:
            pass
        else:
            errores.append(Error(f"Caracter no válido: {char}"))

        i += 1
    
    imprimirLexemasYErrores(lexemas, errores, textAreaFinal)

def imprimirLexemasYErrores(lexemas, errores, textAreaFinal):
    # Imprimimos los lexemas
    textAreaFinal.delete("1.0", END)
    textAreaFinal.insert(END, "#############################\n")
    textAreaFinal.insert(END, "Lexemas:\n")
    for lexema in lexemas:
        textAreaFinal.insert(END, f"{lexema.tipo}: {lexema.valor}\n")
    # Imprimimos los errores
    textAreaFinal.insert(END, "#############################\n")
    textAreaFinal.insert(END, "Errores:\n")
    for error in errores:
        textAreaFinal.insert(END, f"{error.mensaje}\n")

def cargarArchivo(textArea):
    # Abrir un selector de archivos para obtener la data de dicho archivo
    archivo = filedialog.askopenfilename(filetypes=[("Archivo de texto", "*.txt, *.html")])

    # Abrimos el archivo y leemos su contenido
    if archivo:
        # Leemos el archivo seleccionado
        with open(archivo, 'r') as f:
            contenido = f.read()

        # Insertamos el contenido en el text area
        textArea.delete("1.0", END)
        textArea.insert(END, contenido)

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
    ttk.Button(frm, text="Obtener Data", command=lambda: cargarArchivo(textAreaInicial)).grid(column=3, row=0)
    # Creamos un botón para obtener el texto
    ttk.Button(frm, text="Compilar", command=lambda: analizadorLexico(textAreaInicial, textAreaFinal)).grid(column=3, row=1)
    # Creamos un botón para regresar
    ttk.Button(frm, text="Regresar", command=root.destroy).grid(column=3, row=3)

    # Creamos un text area para mostrar los resultados y que no se pueda editar
    textAreaFinal = Text(frm, width=50, height=25)
    textAreaFinal.grid(column=5, row=1)
    #textAreaFinal.config(state=DISABLED)
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