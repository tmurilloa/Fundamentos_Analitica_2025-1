"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open("files/input/data.csv") as data:
        max_letra = {}
        min_letra = {}
        for line in data:
            linea = line.split()
            letra = linea[0]
            valor = int(linea[1])
            
            if letra not in max_letra and letra not in min_letra:
                max_letra[letra] = valor
                min_letra[letra] = valor
            else:
                if valor > max_letra[letra]:
                    max_letra[letra] = valor
                elif valor < min_letra[letra]:
                    min_letra[letra] = valor
        
        resultado = [(letra, max_letra[letra], min_letra[letra]) for letra in sorted(max_letra.keys())]
        return resultado
        

