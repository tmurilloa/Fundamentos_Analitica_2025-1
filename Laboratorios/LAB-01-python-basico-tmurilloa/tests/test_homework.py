"""Autograding script."""

from homework import (
    pregunta_01,
    pregunta_02,
    pregunta_03,
    pregunta_04,
    pregunta_05,
    pregunta_06,
    pregunta_07,
    pregunta_08,
    pregunta_09,
    pregunta_10,
    pregunta_11,
    pregunta_12,
)


def test_pandas():
    """Check if the code imports pandas."""

    def check_imports_pandas(module_path):
        with open(module_path, "r", encoding="utf-8") as file:
            for line in file:
                if "import pandas" in line or "from pandas" in line:
                    return True
        return False

    assert not check_imports_pandas("homework/pregunta_01.py")
    assert not check_imports_pandas("homework/pregunta_02.py")
    assert not check_imports_pandas("homework/pregunta_03.py")
    assert not check_imports_pandas("homework/pregunta_04.py")
    assert not check_imports_pandas("homework/pregunta_05.py")
    assert not check_imports_pandas("homework/pregunta_06.py")
    assert not check_imports_pandas("homework/pregunta_07.py")
    assert not check_imports_pandas("homework/pregunta_08.py")
    assert not check_imports_pandas("homework/pregunta_09.py")
    assert not check_imports_pandas("homework/pregunta_10.py")
    assert not check_imports_pandas("homework/pregunta_11.py")
    assert not check_imports_pandas("homework/pregunta_12.py")


def test_01():
    """Test 01"""
    assert pregunta_01.pregunta_01() == 214


def test_02():
    """Test 02"""
    assert pregunta_02.pregunta_02() == [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]


def test_03():
    """Test 03"""
    assert pregunta_03.pregunta_03() == [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]


def test_04():
    """Test 04"""
    assert pregunta_04.pregunta_04() == [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]


def test_05():
    """Test 05"""
    assert pregunta_05.pregunta_05() == [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]


def test_06():
    """Test 06"""
    assert pregunta_06.pregunta_06() == [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]


def test_07():
    """Test 07"""
    assert pregunta_07.pregunta_07() == [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]


def test_08():
    """Test 08"""
    assert pregunta_08.pregunta_08() == [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]


def test_09():
    """Test 09"""
    assert pregunta_09.pregunta_09() == {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }


def test_10():
    """Test 10"""
    assert pregunta_10.pregunta_10() == [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ("A", 2, 4),
        ("C", 4, 4),
        ("A", 2, 5),
        ("A", 3, 6),
        ("B", 2, 3),
        ("E", 4, 6),
        ("B", 4, 6),
        ("C", 4, 5),
        ("C", 4, 3),
        ("D", 4, 5),
        ("E", 2, 3),
        ("B", 2, 5),
        ("D", 2, 4),
        ("E", 3, 6),
        ("D", 2, 3),
        ("E", 4, 3),
        ("E", 2, 3),
        ("E", 2, 3),
        ("E", 3, 3),
        ("D", 3, 3),
        ("A", 3, 5),
        ("E", 2, 6),
        ("E", 3, 6),
        ("A", 3, 3),
        ("E", 3, 5),
        ("A", 2, 5),
        ("C", 4, 6),
        ("A", 2, 5),
        ("D", 2, 6),
        ("E", 2, 4),
        ("B", 3, 6),
        ("B", 3, 5),
        ("D", 2, 3),
        ("B", 2, 5),
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


def test_11():
    """Test 11"""
    assert pregunta_11.pregunta_11() == {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


def test_12():
    """Test 12"""
    assert pregunta_12.pregunta_12() == {
        "A": 177,
        "B": 187,
        "C": 114,
        "D": 136,
        "E": 324,
    }
