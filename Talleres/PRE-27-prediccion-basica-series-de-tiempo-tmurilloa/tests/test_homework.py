"""Autograding script."""

import os


def test_homework():
    """Test"""

    assert os.path.exists("files/output/metrics.csv")
    assert os.path.exists("files/output/forecasts.csv")
