"""Autograding script."""

import os


def test_homework():
    """Test the homework"""

    assert os.path.exists("homework/linear_regression.py")
    assert os.path.exists("homework/example.py")
