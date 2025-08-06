"""Autograding script."""

from homework import pregunta_01, pregunta_02


def test_01():
    """Test 01"""
    assert pregunta_01.pregunta_01() == "Hola mundo cruel!"


def test_02():
    """Test 02"""
    assert pregunta_02.pregunta_02() == "Hello cruel world!"
