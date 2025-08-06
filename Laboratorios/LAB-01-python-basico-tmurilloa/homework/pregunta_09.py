"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    with open("files/input/data.csv") as data:
        resultado_dic = {}
        for line in data:
            linea = line.split()
            diccionario = linea[4]
            
            clave_valor = diccionario.split(",")
            
            for i in clave_valor:
                clave = i.split(":")[0]
            

                if clave not in resultado_dic:
                    resultado_dic[clave] = 1
                else:
                    resultado_dic[clave] += 1
        

        return dict(sorted(resultado_dic.items()))
                
                
