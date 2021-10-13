from lib.window import ShopWindow
import pytest


@pytest.fixture
def data():
    return {'first': 5, 'second': 4, 'third': 124, 'Iphone 12': 12, 'pc': 5}


@pytest.fixture
def window(qtbot, data):
    return ShopWindow(data_path='..', data=data.copy())
