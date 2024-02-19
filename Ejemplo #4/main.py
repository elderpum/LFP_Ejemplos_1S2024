# Librería a utilizar: pyinstaller

# Comando para generar el ejecutable
# pyinstaller --onefile main.py

salir = False
while (not salir):
    respuesta = input("¿Desea salir? (s/n): ")
    if respuesta == "s":
        salir = True
    elif respuesta == "n":
        salir = False
    else:
        print("Opción incorrecta")