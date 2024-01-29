# Leer archivo pringles.txt

archivo = open("pringles.txt", "r+")

contenido = archivo.read()

archivoPrueba = open("prueba.txt", "w")

archivoPrueba.write(contenido)

archivoPrueba.close()

archivo.close()