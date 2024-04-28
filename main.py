import AppParameters
import gui.LoginWidget
from PyQt5.QtWidgets import QApplication
from flask import request
import sqlite3
import sys
import os



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    start_window = gui.LoginWidget.LoginWidget()
    start_window.show()
    sys.exit(app.exec_())