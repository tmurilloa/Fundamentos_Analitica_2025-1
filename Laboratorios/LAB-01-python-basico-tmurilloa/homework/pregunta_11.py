"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    with open("files/input/data.csv") as data:
        letra_dic = {}
        for line in data:
            linea = line.split()

            valor = int(linea[1])
            col4 = linea[3]
            letras = col4.split(",")
            
            for letra in letras:
                if letra not in letra_dic:
                    letra_dic[letra] = valor
                else:
                    letra_dic[letra] += valor
        
        resultado = dict(sorted(letra_dic.items()))

        return resultado


if __name__ == "__main__":
    print(pregunta_11())
