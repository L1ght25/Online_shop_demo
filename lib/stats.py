from PyQt5.QtWidgets import QLabel, QMainWindow, QPushButton, QWidget


class WindowStats(QMainWindow):

    def __init__(self, data):
        super(WindowStats, self).__init__()

        self.setWindowTitle('Статистика бронирований')

        self.data = data
        self.label = QLabel(
                'Бронирование товаров в магазине\n'.format(self.output_string(self.data)), self
            )
        self.resize(800, 300)  # Тут всего 2 константы, поэтому не стал записывать в отдельный файл
        self.label.resize(800, 100)

    def renew_data(self, data):
        self.label.setText('Бронирование товаров в магазине\n {}'.format(self.output_string(data)))

    @staticmethod
    def output_string(data):
        output = ''
        for element in data.items():
            output += str(element[0]) + ' ---> ' + str(element[1]) + '\n'
        return output
