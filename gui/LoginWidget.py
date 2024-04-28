from gui.compiled.Ui_LoginWidget import Ui_LoginWidget
from PyQt5.QtWidgets import QWidget
from requests import get, post
from gui.TaskWidget import TaskWidget
import config
import json


class LoginWidget(QWidget, Ui_LoginWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()


    def initUI(self):
        self.label.setText("")
        self.deletePushButton.clicked.connect(self.registerButtonClicked)

    def registerButtonClicked(self):
        info = {"login": self.lineEdit.text(), "password": self.lineEdit_2.text()}
        data = get("http://10.16.160.164:5000/signin", json=info)
        getb = data.json()
        if ('AuthKey' in getb.keys()):
            authkey = getb['AuthKey']
            with open('key.txt', 'wt', encoding='utf-8') as file:
                print(authkey, file=file)
            config.authkey = authkey
            self.task = TaskWidget()
            self.task.show()
            self.close()
        else:
            self.label.setText("Неверные данные!")


