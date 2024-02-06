# Libreria Graphviz
# https://graphviz.org/download/
# pip install graphviz

# Libreria Reportlab
# https://www.reportlab.com/dev/install/installation/
# pip install reportlab

# Libreria Tkinter
# https://docs.python.org/3/library/tkinter.html
# pip install tk

from graphviz import Digraph
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def main():
    print("### MENÚ PRINCIPAL ###")
    print("1. Imprimir mis datos")
    print("2. Calcular el área de un círculo")
    print("3. Generar grafo del círculo con Graphviz")
    print("4. Generar PDF del círculo con Reportlab")
    print("5. Exit")
    respuesta = input("Ingrese la opción: ")

    if respuesta == "1":
        print("Nombre: Elder Pum")
        print("Carné: 201700761")
        print("Carrera: Ingeniería en Sistemas")
        print("Correo: ElderPum@gmail.com" )
        main()
    elif respuesta == "2":
        calcularAreaCirculo()
    elif respuesta == "3":
        generarGrafoCirculo()
    elif respuesta == "4":
        generarPDFCirculo()
    elif respuesta == "5":
        print("Hasta luego!")
    else:
        print("Opción inválida")
        main()

def calcularAreaCirculo():
    radio = float(input("Ingrese el radio del círculo: "))
    area = 3.1416 * (radio ** 2)
    print("El área del círculo es: ", area)
    main()

def generarGrafoCirculo():
    radio = float(input("Ingrese el radio del círculo: "))
    dot = Digraph(comment='Grafo del círculo')
    dot.node('A', 'Círculo')
    dot.node('B', 'Área')
    dot.edge('A', 'B', label='r = ' + str(radio))
    dot.render('grafo_circulo', format='png', view=True)
    main()

def generarPDFCirculo():
    w, h = A4
    radio = float(input("Ingrese el radio del círculo: "))
    area = 3.1416 * (radio ** 2)
    c = canvas.Canvas("circulo.pdf", pagesize=A4)
    text = c.beginText(50, h - 50)
    text.textLine("Círculo generado con Graphviz")
    text.textLine("Radio: " + str(radio))
    text.textLine("Área: " + str(area))
    text.textLine()
    c.drawText(text)
    c.drawInlineImage("grafo_circulo.png", 100, 0, width=200, height=300, preserveAspectRatio=True)
    c.save()
    webbrowser.open_new("circulo.pdf")
    main()

main()