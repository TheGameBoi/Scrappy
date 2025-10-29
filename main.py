from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon, QAction
from PyQt6.QtWidgets import (QComboBox, QMessageBox, QPushButton, QLabel, QLineEdit, QGridLayout, QApplication,
                             QMainWindow, QGridLayout, QWidget, QTableWidget, QToolBar, QTextEdit, QStatusBar,
                             QTableWidgetItem, QDialog, QPlainTextEdit, QVBoxLayout, QSizePolicy, QHBoxLayout,
                             QStyleFactory, QFormLayout, QSpinBox, QListWidget)
import sys
from style_sheet import dark_mode_stylesheet
import json


def load_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recycler")
        self.setGeometry(300, 300, 700, 300)
        self.setStyleSheet(dark_mode_stylesheet())


        self.items = load_from_json('items.json')

        master = QWidget(self)
        self.setCentralWidget(master)
        layout = QGridLayout(master)

        self.amount = QSpinBox(self)
        self.amount.setRange(0, 500)

        self.group = QComboBox(self)
        self.group.setFixedWidth(200)
        self.list = QComboBox(self)
        self.list.setFixedWidth(200)

        self.grouping()
        self.listing()

        self.choice = QComboBox(self)
        self.choice.addItem("Safe-Zone")
        self.choice.addItem("Monument")

        self.calculate = QPushButton("Calculate", self)
        self.calculate.clicked.connect(self.calculator)

        self.result = QTextEdit(self)
        self.result.setReadOnly(True)
        self.result.setFixedHeight(125)


        # Add widgets to the layout with labels
        layout.addWidget(self.group, 0, 0)
        layout.addWidget(self.list, 0, 1)
        layout.addWidget(self.choice, 1, 0)
        layout.addWidget(self.amount, 1, 1)
        layout.addWidget(self.calculate, 2, 0, 1, 2)
        layout.addWidget(self.result, 3, 0, 1, 2)

        self.group.currentIndexChanged.connect(self.listing)


    def grouping(self):
        self.group.clear()
        for group in self.items:
            self.group.addItem(group)


    def listing(self):
        selected_group = self.group.currentText()
        if selected_group in self.items:
            for resource in self.items['Components']:
                self.list.addItem(resource)


    def calculator(self):
        resource = self.list.currentText()
        amount = self.amount.value()
        location = self.choice.currentText()
        comps = self.items.get('Components')
        res = comps.get(resource)

        my_dict = {}

        for key, value in res.items():
            if location == 'Safe-Zone':
                my_dict[key] = value * amount * 0.8
            if location == 'Monument':
                my_dict[key] = value * amount * 1.2
        split = ', '.join(f"{int(v)} {k}" for k, v in my_dict.items())
        new_split = [f"{int(v)} {k}" for k, v in my_dict.items()]
        new_var = ""
        for i, v in enumerate(new_split):
            if i == len(new_split) - 1:
                new_var += f'and {v}'
            else:
                new_var += f'{v}, '
        self.result.setText(f"You recycled {amount} {resource} for {new_var} at {location}.")



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())