"""Autograding script."""

import pickle

import pandas as pd
from sklearn.metrics import mean_squared_error


def test_01():
    """Test if the model is able to predict the MPG of a car."""

    dataset = pd.read_csv("files/input/auto_mpg.csv")
    dataset = dataset.dropna()
    dataset["Origin"] = dataset["Origin"].map(
        {1: "USA", 2: "Europe", 3: "Japan"},
    )
    dataset = pd.get_dummies(dataset, columns=["Origin"], prefix="", prefix_sep="")
    y_true = dataset.pop("MPG")

    with open("files/mlp.pickle", "rb") as file:
        mlp = pickle.load(file)

    with open("files/features_scaler.pickle", "rb") as file:
        features_scaler = pickle.load(file)

    standarized_dataset = features_scaler.transform(dataset)
    y_pred = mlp.predict(standarized_dataset)

    mse = mean_squared_error(
        y_true=y_true,
        y_pred=y_pred,
    )

    assert mse < 7.745