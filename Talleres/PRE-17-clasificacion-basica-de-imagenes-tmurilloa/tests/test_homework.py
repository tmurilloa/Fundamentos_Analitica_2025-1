"""Autograding script."""

import os
import pickle

from sklearn import datasets  # type: ignore
from sklearn.metrics import accuracy_score  # type: ignore


def test_01():
    """Test the homework."""

    digits = datasets.load_digits(return_X_y=True)
    data, target = digits

    if not os.path.exists("homework/estimator.pkl"):
        raise FileNotFoundError("homework/estimator.pkl not found")

    with open("homework/estimator.pkl", "rb") as file:
        new_clf = pickle.load(file)

    accuracy = accuracy_score(
        y_true=target,
        y_pred=new_clf.predict(data),
    )

    assert accuracy > 0.96
