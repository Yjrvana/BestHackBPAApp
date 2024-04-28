import datetime

from gui.compiled.Ui_TaskWidget import Ui_TaskWidget
from gui.DescriptionBlockWidget import DescriptionBlockWidget
from gui.ProblemWidget import ProblemWidget
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QScrollBar, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from gui.DataCenterWidget import DataCenterWidget
from requests import get, post
from config import authkey
import json
from datetime import date


class TaskWidget(QWidget, Ui_TaskWidget):
    def __init__(self):
        super().__init__()
        with open('key.txt', 'rt', encoding='utf-8') as file:
            self.authkey = {"AuthKey": int(file.readline().strip())}
        self.setupUi(self)
        self.initUI()


    def initUI(self):
        self.widget = QWidget()
        self.vbox = QVBoxLayout()
        self.vbox.setSpacing(50)

        data = get('http://10.16.160.164:5000/GetTable', json=self.authkey)
        datb = data.json()['table']
        self.go_to_data_center_push_button = QPushButton()
        self.go_to_data_center_push_button.setText("Просмотр статистики")
        self.vbox.addWidget(self.go_to_data_center_push_button)
        for data_block in datb:
            data_parsed_block = dict()
            data_parsed_block['description'] = data_block[0]


            text = "Intent: " + str(data_block[4]) + "\n\n" + data_parsed_block['description']

            pw = ProblemWidget()
            dbw_2 = DescriptionBlockWidget('Description', text)
            pw.addLine(dbw_2)

            self.vbox.addWidget(pw)

        self.widget.setLayout(self.vbox)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.widget)
        self.go_to_data_center_push_button.clicked.connect(self.go_to_data_center)


    def go_to_data_center(self):
        self.DCWidget = DataCenterWidget(self.receive_data_for_n_days(10, self.authkey))
        self.DCWidget.show()
        self.close()


    def receive_data_for_n_days(self, n, authkey):
        data = get('http://10.16.160.164:5000/GetTable', json=authkey)
        datb = data.json()['table']
        today_date = date.today()
        full_result_data = dict()
        for data_block in datb:
            dif = (today_date - self.get_spec_date(data_block[1]).date()).days
            print(data_block)
            if dif > n:
                break
            data_parsed_block = dict()
            if None in data_block:
                continue
            data_parsed_block['description'] = data_block[0]
            data_parsed_block['date_received'] = self.get_spec_date(data_block[1])
            data_parsed_block['date_closed'] = self.get_spec_date(data_block[2])
            data_parsed_block['date_accepted'] = self.get_spec_date(data_block[3])
            full_result_data[dif] = full_result_data.get(dif, []) + [data_parsed_block]
        return full_result_data


    def get_spec_date(self, string):
        return datetime.datetime.strptime(string, '%a, %d %b %Y %H:%M:%S GMT')


