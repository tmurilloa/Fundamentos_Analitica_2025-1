"""Autograding script."""

import os

import pandas as pd  # type: ignore

from homework.country_collaboration import make_plot


def test_01():
    """Test the country_collaboration module."""

    make_plot(n_countries=20)

    #
    # Retorna error si la carpeta output/ no existe
    if not os.path.exists("files/countries.csv"):
        raise FileNotFoundError("File 'files/countries.csv' not found")

    #
    # Lee el contenido del archivo output.txt
    dataframe = pd.read_csv("files/countries.csv")
    dataframe = dataframe.set_index("countries")

    assert dataframe["count"]["United States"] == 579
    assert dataframe["count"]["China"] == 273
    assert dataframe["count"]["India"] == 174
    assert dataframe["count"]["United Kingdom"] == 173
    assert dataframe["count"]["Italy"] == 112

    #
    #
    if not os.path.exists("files/co_occurrences.csv"):
        raise FileNotFoundError("File 'files/co_occurrences.csv' not found")

    if not os.path.exists("files/network.png"):
        raise FileNotFoundError("File 'files/network.pmg' not found")
