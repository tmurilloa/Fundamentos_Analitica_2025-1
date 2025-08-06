"""Autograding script"""

import os


def test_01():
    """Test 01."""

    assert os.path.exists("homework/train_model.py")
    assert os.path.exists("homework/web_app.py")
    assert os.path.exists("homework/api_client.py")
    assert os.path.exists("homework/api_server.py")
    assert os.path.exists("homework/descriptivo.ipynb")
    assert os.path.exists("homework/house_predictor.pkl")
