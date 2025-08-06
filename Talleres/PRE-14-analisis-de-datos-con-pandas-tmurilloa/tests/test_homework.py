"""Autograding script."""

import os


def test_homework():
    """Test homework"""
    assert os.path.exists("files/images/delays_by_carrier.png")
    assert os.path.exists("files/images/delays_by_day_of_week.png")
    assert os.path.exists("files/images/delays_by_hour_of_day.png")
