from test_window_fixtures import data, window
from PyQt5 import QtCore


def test_buttons_start(data, window):
    assert len(window.button) == len(window.data)  # Проверка на кол-во кнопок


def test_text(data, window):
    assert window.windowTitle() == 'Интернет-магазин'  # Проверка на блок текста (Заголовок окна)


def test_buttons_text(data, window):
    for key in window.data:
        assert '{} \n Кол-во: {}'.format(key, window.data[key]) == window.button[key].text()  # Текст кнопок


def test_push_buttons(qtbot, data, window):
    for key in window.data:
        qtbot.mouseClick(window.button[key], QtCore.Qt.LeftButton)
        qtbot.mouseClick(window.button[key], QtCore.Qt.LeftButton)
        assert window.button[key].text() == '{} \n Кол-во: {}'.format(key, data[key] - 2)  # Проверка
        # нажимания на кнопки


def test_sort_buttons(window):
    values = list(window.data.values())
    if not all(values[i] <= values[i + 1] for i in range(len(values) - 1)):
        raise AssertionError  # Проверка на отсортированные кнопки


def test_zero_of_button(qtbot, window):
    for key in window.data:
        while window.data[key] != 0:
            qtbot.mouseClick(window.button[key], QtCore.Qt.LeftButton)
        if key in window.button:
            raise AssertionError  # Проверка того, что кнопка исчезла после достижения 0
