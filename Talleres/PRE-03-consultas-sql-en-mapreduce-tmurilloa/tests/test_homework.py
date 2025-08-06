"""Autograding script."""

# pylint: disable=broad-exception-raised
# pylint: disable=import-error

import os

from homework.queries import run


def test_01():
    """Test the homework."""

    run()

    for directory in [
        "files/query_1/",
        "files/query_2/",
        "files/query_3/",
        "files/query_4/",
        "files/query_5/",
    ]:
        for file in [
            "_SUCCESS",
            "part-00000",
        ]:

            filename = directory + file

            if not os.path.exists(filename):
                raise Exception(f"The file {filename} does not exist")
