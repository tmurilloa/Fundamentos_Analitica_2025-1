"""Autograding script."""

# pylint: disable=broad-exception-raised

import os

import homework.word_count as wc


def test_01():
    """Test Word Count"""

    wc.copy_raw_files_to_input_folder(n=1000)
    wc.run_job(
        "files/input",
        "files/output",
    )

    #
    # Retorna error si la carpeta output/ no existe
    if not os.path.exists("files/output/"):
        raise Exception("Output directory does not exist")

    #
    # Retorna error si el archivo "_SUCCESS" no existe en la
    # carpeta output/
    if not os.path.exists("files/output/_SUCCESS"):
        raise Exception("Output directory is empty")

    #
    # Lee el contenido del archivo "part-00000" en la carpeta output/
    # Cada linea en el archivo esta conformada por una clave un valor,
    # separados por un tabulador. Asigne pareja a un diccionario
    with open("files/output/part-00000", "r", encoding="utf-8") as f:
        lines = f.readlines()
        result = {}
        for line in lines:
            key, value = line.strip().split("\t")
            result[key] = int(value)

    assert result["analytics"] == 5000
    assert result["business"] == 7000
    assert result["by"] == 3000
    assert result["algorithms"] == 2000
    assert result["analysis"] == 4000
