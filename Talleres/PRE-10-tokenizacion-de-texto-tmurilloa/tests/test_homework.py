"""Autograding script."""

import os


def test_homework():
    """Test homework."""
    assert os.path.exists("files/output/file1.txt")
    assert os.path.exists("files/output/file2.txt")
    assert os.path.exists("files/output/file3.txt")
