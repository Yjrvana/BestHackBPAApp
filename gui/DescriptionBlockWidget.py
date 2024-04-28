from PyQt5 import QtWidgets

from gui.compiled.Ui_DescriptionBlockWidget import Ui_DescriptionBlockWidget
from PyQt5.QtWidgets import QWidget, QAbstractScrollArea
from requests import get, post
import json


class DescriptionBlockWidget(QWidget, Ui_DescriptionBlockWidget):
    def __init__(self, k, v):
        super().__init__()
        self.k = str(k)
        self.v = str(v)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.textBrowser_1.setText(self.v)




