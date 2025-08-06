"""Autograding script."""

import os

import pandas as pd  # type: ignore

from homework.country_scientific_production import make_worldmap


def test_01():
    """Test country_scientific_production.py."""

    make_worldmap()

    #
    # Retorna error si la carpeta output/ no existe
    if not os.path.exists("files/countries.csv"):
        raise FileNotFoundError("File 'files/countries.csv' not found")

    #
    # Lee el contenido del archivo output.txt
    dataframe = pd.read_csv("files/countries.csv")
    dataframe = dataframe.set_index("countries")

    assert dataframe["count"]["United States of America"] == 579
    assert dataframe["count"]["China"] == 273
    assert dataframe["count"]["India"] == 174
    assert dataframe["count"]["United Kingdom"] == 173
    assert dataframe["count"]["Italy"] == 112

    if not os.path.exists("files/map.html"):
        raise FileNotFoundError("File 'files/map.html' not found")
