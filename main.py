import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, \
    QHBoxLayout, QVBoxLayout, QWidget, QLabel, QFormLayout, QLineEdit

alph = 'А Б В Г Д Е Ё Ж З И К Л М Н О П Р С Т'
app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.is_toggled = True
        self.button_is_checked = True
        self.setWindowTitle("Hello!")
        self.setFixedSize(QSize(920, 480))

        self.play = QPushButton('Играть')
        self.settings = QPushButton('Настройки')

        self.play.setCheckable(True)
        self.settings.setCheckable(True)

        self.play.clicked.connect(self.play_clicked)
        self.settings.clicked.connect(self.settings_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.play, 2)
        layout.addWidget(self.settings, 0)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def play_clicked(self):
        layout1 = QVBoxLayout()

        layout = QHBoxLayout()

        label = QLabel()
        label.setText('Доступные буквы:')
        label.adjustSize()
        layout.addWidget(label)

        letters = QLabel()
        letters.setText(alph)
        letters.adjustSize()
        layout.addWidget(letters)

        layout1.addLayout(layout)

        layout2 = QFormLayout()
        layout.addWidget(QLineEdit)

        container = QWidget()
        container.setLayout(layout1)
        self.setCentralWidget(container)

    def settings_clicked(self):
        pass


window = MainWindow()
window.show()

app.exec()
