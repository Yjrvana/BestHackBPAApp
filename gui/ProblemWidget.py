from gui.compiled.Ui_ProblemWidget import Ui_ProblemWidget
from PyQt5.QtWidgets import QWidget
from requests import get, post
import json


class ProblemWidget(QWidget, Ui_ProblemWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()


    def initUI(self):
        pass

    def addLine(self, dblockw):
        self.verticalLayout_2.addWidget(dblockw)

    def acceptButtonClicked(self):
        pass
