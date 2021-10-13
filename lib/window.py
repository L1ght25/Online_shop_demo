import yaml
from PyQt5.QtWidgets import QLabel, QMainWindow, QPushButton, QWidget, QInputDialog
from lib.stats import WindowStats
import os


class ShopWindow(QMainWindow):

    def __init__(self, data_path='', data=None):
        super(ShopWindow, self).__init__()

        self.setWindowTitle('Интернет-магазин')
        self.data_flag = data

        if self.data_flag is not None:
            self.data = data
        else:
            with open(os.path.join(data_path, 'data/data.yml'), 'r') as file:
                self.data = yaml.safe_load(file)
        with open(os.path.join(data_path, 'data/buttons.yml'), 'r') as file:
            self.geometry = yaml.safe_load(file)
        with open(os.path.join(data_path, 'data/size_of_window.yml'), 'r') as file:
            self.size_of_window = yaml.safe_load(file)
        with open(os.path.join(data_path, 'data/booked_items.yml'), 'r') as file:
            self.have_booked = yaml.safe_load(file)

        self.data = dict(sorted(self.data.items(), key=lambda item: item[1]))
        self.button = {}
        if data is None:
            self.name = QInputDialog.getText(
                self, 'Input Dialog', 'Enter your name:')[0]
        else:
            self.name = 'TEST_MODE'
        if self.name not in self.have_booked:
            self.have_booked[self.name] = {}

        curr_geometry = 0
        for key in self.data:
            if self.data[key] >= 1:
                self.button[key] = QPushButton(key, self)
                self.button[key].setGeometry(*self.geometry[curr_geometry])
                self.button[key].clicked.connect(self.on_click)
                self.button[key].setText('{} \n Кол-во: {}'.format(key, self.data[key]))
                curr_geometry += 1
            # self.have_booked[self.name] = {}

        self.button_of_stats = QPushButton('Статистика брони', self)
        self.button_of_stats.setGeometry(*self.geometry[-1])
        self.button_of_stats.clicked.connect(self.on_click_stats)

        self.sides_of_button = self.geometry[0]

        self.data_path = data_path

        self.resize(*self.size_of_window)

        self.second_window = WindowStats(self.have_booked)

    def on_click(self):
        sender = self.sender()
        key = sender.text().split('\n')[0][:-1]
        self.data[key] -= 1
        if key in self.have_booked[self.name]:
            self.have_booked[self.name][key] += 1
        else:
            self.have_booked[self.name][key] = 1

        with open(os.path.join(self.data_path, 'data/booked_items.yml'), 'w') as file:
            yaml.dump(self.have_booked, file)

        if self.data[key] == 0:
            self.button[key].deleteLater()
            self.button.pop(key)
        else:
            self.button[key].setText('{} \n Кол-во: {}'.format(key, self.data[key]))

        if self.data_flag is None:
            with open(os.path.join(self.data_path, 'data/data.yml'), 'w') as file:
                yaml.dump(self.data, file)

        self.sort_buttons()

    def on_click_stats(self):
        self.second_window.renew_data(self.have_booked)
        self.second_window.show()

    def sort_buttons(self):
        self.data = dict(sorted(self.data.items(), key=lambda item: item[1]))
        left_side = 0
        for key in self.data:
            if key in self.button:
                self.button[key].setGeometry(left_side, *self.sides_of_button[1:])
                left_side += 200

