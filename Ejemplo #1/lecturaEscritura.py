# Obtener la data de pringles.txt y pasarlo al backup

archivo = open("pringles.txt", "r+")

contenido = archivo.read()

archivo.close()

archivoBackup = open("backup.lfp", "w+")

archivoBackup.write(contenido)

archivoBackup.close()

# Leer el backup y pasarlo a un archivo nuevo

archivoFinal = open("backup.lfp", "r+")

contenidoFinal = archivoFinal.read()

archivoNuevo = open("archivoProduccion.xdd", "w+")

archivoNuevo.write(contenidoFinal)

archivoNuevo.close()

archivoFinal.close()