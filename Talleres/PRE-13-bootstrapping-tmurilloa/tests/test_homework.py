"""Autograding script"""

import os


def test_01():
    """Test the homework."""
    assert os.path.exists("files/results/experiments.csv")
    assert os.path.exists("files/results/stats.csv")
    assert os.path.exists("files/results/stats.txt")
