"""Autograding script."""


def load_data():

    import pandas as pd

    dataset = pd.read_csv("auto_mpg.csv")
    dataset = dataset.dropna()
    dataset["Origin"] = dataset["Origin"].map(
        {1: "USA", 2: "Europe", 3: "Japan"},
    )
    y = dataset.pop("MPG")
    x = dataset.copy()

    return x, y


def load_estimator():

    import os
    import pickle

    if not os.path.exists("estimator.pickle"):
        return None
    with open("estimator.pickle", "rb") as file:
        estimator = pickle.load(file)

    return estimator


def test_01():

    from sklearn.metrics import accuracy_score

    x, y = load_data()
    estimator = load_estimator()

    accuracy = accuracy_score(
        y_true=y,
        y_pred=estimator.predict(x),
    )

    assert accuracy > 0.9545
