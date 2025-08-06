"""Autograding script."""

import os

import pandas as pd  # type: ignore

from homework import clean_data  # type: ignore


def test_homework():
    """Test homework/clean_data.py"""

    clean_data.main(
        "files/input.txt",
        "files/output.txt",
    )

    if not os.path.exists("files/test.csv"):
        raise FileNotFoundError("File 'files/test.csv' not found")

    test = pd.read_csv("files/test.csv", index_col=None)

    assert test.loc[0, "key"] == "analyt applic"
    assert test.loc[6, "key"] == "analyt model"
    assert test.loc[9, "key"] == "adhoc queri"
    assert test.loc[11, "key"] == "agricultur product"
    assert test.loc[16, "key"] == "airlin compani"
    assert test.loc[25, "key"] == "adhoc queri"

    #
    # Retorna error si la carpeta output/ no existe
    if not os.path.exists("files/output.txt"):
        raise FileNotFoundError("File 'files/output.txt' not found")

    #
    # Lee el contenido del archivo output.txt
    dataframe = pd.read_csv("files/output.txt")
    count = dataframe.groupby("cleaned_text").size()

    assert count.loc["ADHOC QUERIES"] == 6
    assert count.loc["AGRICULTURAL PRODUCTS"] == 5
    assert count.loc["AIRLINE COMPANY"] == 4
    assert count.loc["AIRLINES"] == 1
    assert count.loc["ANALYTICS MODEL"] == 10
    assert count.loc["Analytics Application"] == 9
