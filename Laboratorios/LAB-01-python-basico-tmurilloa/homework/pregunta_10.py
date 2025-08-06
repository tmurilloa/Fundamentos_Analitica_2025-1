"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    with open("files/input/data.csv") as data:
        lista_complt = []
        for line in data:
            linea = line.split()
            letra = linea[0]

            col4 = linea[3]
            col4 = col4.split(",")
            col5 = linea[4]
            col5 = col5.split(",")

            lista_complt.append((letra, len(col4), len(col5)))

        return lista_complt
    
if __name__ == "__main__":
    print(pregunta_10())



