import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from gui.compiled.Ui_TaskWidget import Ui_TaskWidget

from requests import get
import gui.TaskWidget
from PyQt5 import QtWidgets, QtGui
import matplotlib
import config
from PyQt5.QtCore import Qt
import json


class DataCenterWidget(QWidget, Ui_TaskWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.create_graphs(self.organize_data(self.data))
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.widget = QWidget()

        self.vbox = QVBoxLayout()
        self.vbox.setSpacing(50)
        self.label = QLabel(self)
        self.pix = QtGui.QPixmap('im_1.png')
        self.label.setPixmap(self.pix)
        self.vbox.addWidget(self.label)
        self.label_1 = QLabel(self)
        self.pix_1 = QtGui.QPixmap('im_2.png')
        self.label_1.setPixmap(self.pix_1)
        self.vbox.addWidget(self.label_1)

        self.widget.setLayout(self.vbox)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.widget)


    def organize_data(self, data):
        result = dict()
        for p in data.items():
            dat_block_1 = [0, 0]
            k = 0
            for d in p[1]:
                dat_block_1[0] += (d['date_accepted'] - d['date_received']).days
                dat_block_1[1] += (d['date_closed'] - d['date_received']).days
                k += 1
            dat_block_1[0] //= k
            dat_block_1[1] //= k
            result[p[0]] = dat_block_1
        print('result: ', result)
        return result


    def create_graphs(self, org_data):
        dat_1 = org_data.keys()
        bgh = org_data.values()
        dat_2 = list(map(lambda p: p[0], bgh))
        dat_3 = list(map(lambda p: p[1], bgh))

        print(dat_1)
        print(dat_2)
        print(dat_3)

        plt.bar(dat_1, dat_2)
        plt.savefig('im_1.png')

        plt.bar(dat_1, dat_3)
        plt.savefig('im_2.png')



    def registerButtonClicked(self):
        info = {"login": self.lineEdit.text(), "password": self.lineEdit_2.text()}
        data = get("http://10.16.160.164:5000/signin", json=info)
        getb = data.json()
        if ('AuthKey' in getb.keys()):
            authkey = getb['AuthKey']
            with open('key.txt', 'wt', encoding='utf-8') as file:
                print(authkey, file=file)
            config.authkey = authkey
            self.task = gui.TaskWidget.TaskWidget()
            self.task.show()
            self.close()
        else:
            self.label.setText("Неверные данные!")


