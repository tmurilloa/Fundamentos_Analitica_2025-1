# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""Autograding script."""

import os.path

import pandas as pd  # type: ignore

from homework import pregunta_01 as pregunta


def test_01():
    """Test homework"""

    pregunta.pregunta_01()

    if not os.path.exists("files/output/train_dataset.csv"):
        raise FileNotFoundError("File 'files/output/train_dataset.csv' not found")

    train_dataset = pd.read_csv("files/output/train_dataset.csv")

    assert "phrase" in train_dataset.columns
    assert "target" in train_dataset.columns

    counts = train_dataset["target"].value_counts()

    assert counts["neutral"] == 1117
    assert counts["positive"] == 458
    assert counts["negative"] == 236

    if not os.path.exists("files/output/test_dataset.csv"):
        raise FileNotFoundError("File 'files/output/test_dataset.csv' not found")

    test_dataset = pd.read_csv("files/output/test_dataset.csv")

    assert "phrase" in test_dataset.columns
    assert "target" in test_dataset.columns

    counts = test_dataset["target"].value_counts()

    assert counts["neutral"] == 274
    assert counts["positive"] == 112
    assert counts["negative"] == 67
