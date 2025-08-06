# flake8: noqa: E501
"""Autograding script."""

import gzip
import json
import os
import pickle

import pandas as pd  # type: ignore

# ------------------------------------------------------------------------------
MODEL_FILENAME = "files/models/model.pkl.gz"
MODEL_COMPONENTS = [
    "OneHotEncoder",
    "PCA",
    "StandardScaler",
    "SelectKBest",
    "SVC",
]
SCORES = [
    0.661,
    0.666,
]
METRICS = [
    {
        "type": "metrics",
        "dataset": "train",
        "precision": 0.691,
        "balanced_accuracy": 0.661,
        "recall": 0.370,
        "f1_score": 0.482,
    },
    {
        "type": "metrics",
        "dataset": "test",
        "precision": 0.673,
        "balanced_accuracy": 0.661,
        "recall": 0.370,
        "f1_score": 0.482,
    },
    {
        "type": "cm_matrix",
        "dataset": "train",
        "true_0": {"predicted_0": 15440, "predicted_1": None},
        "true_1": {"predicted_0": None, "predicted_1": 1735},
    },
    {
        "type": "cm_matrix",
        "dataset": "test",
        "true_0": {"predicted_0": 6710, "predicted_1": None},
        "true_1": {"predicted_0": None, "predicted_1": 730},
    },
]


# ------------------------------------------------------------------------------
#
# Internal tests
#
def _load_model():
    """Generic test to load a model"""
    assert os.path.exists(MODEL_FILENAME)
    with gzip.open(MODEL_FILENAME, "rb") as file:
        model = pickle.load(file)
    assert model is not None
    return model


def _test_components(model):
    """Test components"""
    assert "GridSearchCV" in str(type(model))
    current_components = [str(model.estimator[i]) for i in range(len(model.estimator))]
    for component in MODEL_COMPONENTS:
        assert any(component in x for x in current_components)


def _load_grading_data():
    """Load grading data"""
    with open("files/grading/x_train.pkl", "rb") as file:
        x_train = pickle.load(file)

    with open("files/grading/y_train.pkl", "rb") as file:
        y_train = pickle.load(file)

    with open("files/grading/x_test.pkl", "rb") as file:
        x_test = pickle.load(file)

    with open("files/grading/y_test.pkl", "rb") as file:
        y_test = pickle.load(file)

    return x_train, y_train, x_test, y_test


def _test_scores(model, x_train, y_train, x_test, y_test):
    """Test scores"""
    assert model.score(x_train, y_train) > SCORES[0]
    assert model.score(x_test, y_test) > SCORES[1]


def _load_metrics():
    assert os.path.exists("files/output/metrics.json")
    metrics = []
    with open("files/output/metrics.json", "r", encoding="utf-8") as file:
        for line in file:
            metrics.append(json.loads(line))
    return metrics


def _test_metrics(metrics):

    for index in [0, 1]:
        assert metrics[index]["type"] == METRICS[index]["type"]
        assert metrics[index]["dataset"] == METRICS[index]["dataset"]
        assert metrics[index]["precision"] > METRICS[index]["precision"]
        assert metrics[index]["balanced_accuracy"] > METRICS[index]["balanced_accuracy"]
        assert metrics[index]["recall"] > METRICS[index]["recall"]
        assert metrics[index]["f1_score"] > METRICS[index]["f1_score"]

    for index in [2, 3]:
        assert metrics[index]["type"] == METRICS[index]["type"]
        assert metrics[index]["dataset"] == METRICS[index]["dataset"]
        assert (
            metrics[index]["true_0"]["predicted_0"]
            > METRICS[index]["true_0"]["predicted_0"]
        )
        assert (
            metrics[index]["true_1"]["predicted_1"]
            > METRICS[index]["true_1"]["predicted_1"]
        )


def test_homework():
    """Tests"""

    model = _load_model()
    x_train, y_train, x_test, y_test = _load_grading_data()
    metrics = _load_metrics()

    _test_components(model)
    _test_scores(model, x_train, y_train, x_test, y_test)
    _test_metrics(metrics)
