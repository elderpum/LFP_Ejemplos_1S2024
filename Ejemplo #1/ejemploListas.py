def arrayTemporal(arrayTemporal):
    for i in range(10):
        arrayTemporal.append(i)

    return arrayTemporal

def main():
    lista1 = [1, 2, 3, 4, 5]

    # Imprimir la lista
    print(lista1)

    # Imprimir el primer elemento de la lista
    print(lista1[0])

    # Imprimir el último elemento de la lista
    print(lista1[-1])

    # Imprimir uno por uno los elementos de la lista
    for i in lista1:
        print(i)

def main2():
    lista2 = ["Perro", "Gato", "Conejo", "Pez", "Loro"]

    # Imprimir la lista
    print(lista2)

    # Agregar un elemento a la lista
    lista2.append("Tortuga")
    lista2.append(100)
    lista2.append(3.1416)
    lista2.append(True)

    # Imprimir la lista
    print(lista2)

    arrayTemp = []

    lista2 = lista2 + ['c', arrayTemporal(arrayTemp)]
    print(lista2)

    print(len(lista2))

    print(lista2[10][9])

    dic = {'nombre': 'Carlos', 'edad': 22, 'cursos': ['Python', 'Java', 'C++']}

    print(dic['nombre'])

    print(dic['cursos'][1])

    # Imprimir por valor y no por llave
    print(dic.values())

main2()