# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import glob
import os
import pandas as pd

def load_input(target, input_directory):
    files = glob.glob(f"{input_directory}/*.txt")
    datos = []

    for file in files:
        with open(file, "r") as f:
            contenido = f.read()
            datos.append({"phrase": contenido, "target": target})
    
    df_textos = pd.DataFrame(datos)
    return df_textos


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    # Dataframes de datos tests
    dataframe_test_negative = load_input("negative", "files/input/test/negative")

    dataframe_test_neutral = load_input("neutral", "files/input/test/neutral")

    dataframe_test_positive = load_input("positive", "files/input/test/positive")

    df_test = pd.concat(
        [dataframe_test_negative, dataframe_test_neutral, dataframe_test_positive],
        ignore_index=True
    )

    # Dataframes de datos train
    dataframe_train_negative = load_input("negative", "files/input/train/negative")

    dataframe_train_neutral = load_input("neutral", "files/input/train/neutral")

    dataframe_train_positive = load_input("positive", "files/input/train/positive")

    df_train = pd.concat(
        [dataframe_train_negative, dataframe_train_neutral, dataframe_train_positive],
        ignore_index=True
    )

    os.makedirs("files/output", exist_ok=True)

    df_train.to_csv("files/output/train_dataset.csv", index=False)
    df_test.to_csv("files/output/test_dataset.csv", index=False)



