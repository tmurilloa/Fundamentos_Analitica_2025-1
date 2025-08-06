"""Autograding script."""

import os

from homework import pregunta_01 as pregunta


def test_01():
    """Test homework"""

    if os.path.exists("files/plots/news.png"):
        os.remove("files/plots/news.png")
        os.removedirs("files/plots")

    pregunta.pregunta_01()

    assert os.path.exists("files/plots/news.png")
