"""Autograding script."""

import os


def test_01():
    """Test 01"""
    assert os.path.exists("files/output/specific-columns.csv")
