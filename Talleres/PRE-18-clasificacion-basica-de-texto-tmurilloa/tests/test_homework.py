"""Autograding script."""

import pickle

import pandas as pd  # type: ignore
from sklearn.metrics import accuracy_score  # type: ignore


def test_01():
    """Test the homework."""

    dataframe = pd.read_csv(
        "files/input/sentences.csv.zip",
        index_col=False,
        compression="zip",
    )

    with open("homework/clf.pickle", "rb") as file:
        clf = pickle.load(file)

    with open("homework/vectorizer.pkl", "rb") as file:
        vectorizer = pickle.load(file)

    accuracy = accuracy_score(
        y_true=dataframe.target,
        y_pred=clf.predict(vectorizer.transform(dataframe.phrase)),
    )

    assert accuracy > 0.854
