import sys
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader


def play(row, col):
    buttons[row][col].setText("X")



app = QApplication(sys.argv)

loader = QUiLoader()
main_window = loader.load("main_window.ui")
main_window.show()
main_window.btn_1.clicked.connect(partial(play, 0, 0))
main_window.btn_2.clicked.connect(partial(play, 0, 1))
main_window.btn_3.clicked.connect(partial(play, 0, 2))
main_window.btn_4.clicked.connect(partial(play, 1, 0))
main_window.btn_5.clicked.connect(partial(play, 1, 1))
main_window.btn_6.clicked.connect(partial(play, 1, 2))
main_window.btn_7.clicked.connect(partial(play, 2, 0))
main_window.btn_8.clicked.connect(partial(play, 2, 1))
main_window.btn_9.clicked.connect(partial(play, 2, 2))

buttons = [[main_window.btn_1, main_window.btn_2, main_window.btn_3],
           [main_window.btn_4, main_window.btn_5, main_window.btn_6],
           [main_window.btn_7, main_window.btn_8, main_window.btn_9]]




app.exec()
