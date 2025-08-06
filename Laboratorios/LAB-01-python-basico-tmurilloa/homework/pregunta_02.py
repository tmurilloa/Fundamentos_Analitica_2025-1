"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    with open("files/input/data.csv") as data:
        letras = {}
        for line in data:
            linea = line.split()
            if linea[0] not in letras:
                letras[linea[0]] = 1
            else:
                letras[linea[0]] += 1
        resultado = list(letras.items())
        return sorted(resultado)
        

if __name__ == "__main__":
    resultado = pregunta_02()
    print(resultado)