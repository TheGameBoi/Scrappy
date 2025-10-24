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
        self.setWindowTitle("Scrappy")
        self.setGeometry(300, 300, 700, 300)
        self.setStyleSheet(dark_mode_stylesheet())

        self.items = load_from_json('items.json')


        master = QWidget(self)
        self.setCentralWidget(master)
        layout = QFormLayout(master)


        self.amount = QSpinBox(self)
        self.amount.setRange(0, 500)


        self.group = QComboBox(self)
        self.list = QComboBox(self)
        self.grouping()
        self.listing()


        self.choice = QComboBox(self)
        self.choice.addItem("Safe-Zone")
        self.choice.addItem("Monument")


        self.calculate = QPushButton("Calculate", self)
        self.calculate.clicked.connect(self.calculator)

        self.result = QTextEdit(self)
        self.result.setReadOnly(True)


        # Add widgets to the layout with labels
        layout.addRow("Group:", self.group)
        layout.addRow("Item:", self.list)
        layout.addRow("Location:", self.choice)
        layout.addRow("Amount:", self.amount)
        layout.addRow(self.calculate)
        layout.addRow(self.result)

        self.group.currentIndexChanged.connect(self.listing)


        # Add some spacing and padding
        layout.setVerticalSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)



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
            my_dict[key] = value * amount * 0.8
            if location == 'Monument':
                my_dict[key] = value * amount * 1.2

        resources = ""
        for key, value in my_dict.items():
            resources += f"{int(value)} {key} "

        self.result.setText(f"You recycled {amount} {resource} for: {resources}at {location}.")




app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())