# Escribir en un archivo
archivo = open("pringles.txt", "r+")

receta = '1. Agarrar una papa\n2. Cortar la papa\n3. Freir la papa\n4. Agregar sal\n5. Comer'

archivo.write(receta)

archivo.close()