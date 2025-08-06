"""Autograding script."""

import os


def test_homework():
    """Test the homework."""

    assert os.path.exists(
        "files/data/demanda-comercial-dias.csv"
    ), "files/data/demanda-comercial-dias.csv file is missing"

    assert os.path.exists(
        "files/plots/demanda-comercial-patrones-ejemplo.png"
    ), "files/plots/demanda-comercial-patrones-ejemplo.png file is missing"

    assert os.path.exists(
        "files/plots/demanda-comercial-perfiles.png"
    ), "files/plots/demanda-comercial-perfiles.png file is missing"

    assert os.path.exists(
        "files/plots/demanda-comercial.png"
    ), "files/plots/demanda-comercial.png file is missing"
