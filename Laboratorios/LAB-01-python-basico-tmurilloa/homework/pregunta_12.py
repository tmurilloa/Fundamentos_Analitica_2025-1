"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open("files/input/data.csv") as data:
        col1_sumCol5 = {}
        for line in data:
            linea = line.split()

            clave = linea[0]
            col5 = linea[4]

            clave_valor = col5.split(",")
            acum_valor = 0
            for i in clave_valor:
                valor = int(i.split(":")[1])
                acum_valor += valor
            
            if clave not in col1_sumCol5:
                col1_sumCol5[clave] = acum_valor
            else:
                col1_sumCol5[clave] += acum_valor
        
        resultado = dict(sorted(col1_sumCol5.items()))

        return resultado
    
if __name__ == "__main__":
    print(pregunta_12())
            

