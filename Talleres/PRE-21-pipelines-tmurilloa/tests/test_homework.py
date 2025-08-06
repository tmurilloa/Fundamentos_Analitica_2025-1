"""Autograding script."""

import pickle

import pandas as pd
from sklearn.metrics import accuracy_score


def load_data():

    import pandas as pd

    dataframe = pd.read_csv(
        "files/input/sentences.csv.zip",
        index_col=False,
        compression="zip",
    )

    data = dataframe.phrase
    target = dataframe.target

    return data, target


def load_estimator():

    import os
    import pickle

    if not os.path.exists("homework/estimator.pickle"):
        return None
    with open("homework/estimator.pickle", "rb") as file:
        estimator = pickle.load(file)

    return estimator


def test_homework():

    data, target = load_data()
    estimator = load_estimator()

    accuracy = accuracy_score(
        y_true=target,
        y_pred=estimator.predict(data),
    )

    assert accuracy > 0.8555
