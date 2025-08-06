"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    with open("files/input/data.csv") as data:
        max_clave = {}
        min_clave = {}
        for line in data:
            linea = line.split()
            clave_valor = linea[4].split(",")
            for i in clave_valor:
                cv = i.split(":")
                clave =  cv[0]
                valor = int(cv[1])
                if clave not in max_clave and clave not in min_clave:
                    max_clave[clave] = valor
                    min_clave[clave] = valor
                else:
                    if valor > max_clave[clave]:
                        max_clave[clave] = valor
                    elif valor < min_clave[clave]:
                        min_clave[clave] = valor
        
        resultado = [(clave, min_clave[clave], max_clave[clave]) for clave in sorted(max_clave.keys())]
        return resultado

        