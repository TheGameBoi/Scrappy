import sys
import json
from style_sheet import dark_mode_stylesheet
from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon, QAction
from PyQt6.QtWidgets import (QComboBox, QMessageBox, QPushButton, QLabel, QLineEdit, QGridLayout, QApplication,
                             QMainWindow, QGridLayout, QWidget, QTableWidget, QToolBar, QTextEdit, QStatusBar,
                             QTableWidgetItem, QDialog, QPlainTextEdit, QVBoxLayout, QSizePolicy, QHBoxLayout,
                             QStyleFactory, QFormLayout, QSpinBox, QListWidget, QMenu)



def load_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recycler")
        self.setWindowIcon(QIcon('imgs/recycler.ico'))
        self.setGeometry(300, 300, 680, 280)
        self.setStyleSheet(dark_mode_stylesheet())

        self.items = load_from_json('items.json')

        master = QWidget(self)
        self.setCentralWidget(master)
        layout = QGridLayout(master)

        self.setStatusBar(QStatusBar(master))
        self.menuBar()

        self.file_menu = self.menuBar().addMenu('&File')
        self.file_help = QAction('Help', self)
        self.file_menu.addAction(self.file_help)
        self.file_help.triggered.connect(self.help)
        self.file_bug = QAction('Report a Bug', self)
        self.file_menu.addAction(self.file_bug)
        self.file_menu.triggered.connect(self.debugger)


        self.about_menu = self.menuBar().addMenu('&About')
        self.about_action = QAction('Info', self)
        self.about_menu.addAction(self.about_action)
        self.about_action.triggered.connect(self.about)

        self.amount = QSpinBox(self)
        self.amount.setRange(0, 500)

        self.group = QComboBox(self)
        self.group.setFixedWidth(200)
        self.group.currentIndexChanged.connect(self.listing)
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
        self.result.setFixedHeight(70)

        # Add widgets to the layout
        layout.addWidget(self.group, 0, 0)
        layout.addWidget(self.list, 0, 1)
        layout.addWidget(self.choice, 1, 0)
        layout.addWidget(self.amount, 1, 1)
        layout.addWidget(self.calculate, 2, 0, 1, 2)
        layout.addWidget(self.result, 3, 0, 1, 2)


    def about(self):
        dialog = AboutDialog()
        dialog.exec()

    def help(self):
        dialog = HelpDialog()
        dialog.exec()

    def debugger(self):
        self.debug = BugReport()
        self.debug.show()


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



class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About Us")
        self.setGeometry(300, 300, 400, 300)
        self.setWindowIcon(QIcon('imgs/info.ico'))
        contents = ("Scrappy v0.1" + "\n"
                   "Made by TheGameBoi")
        self.setText(contents)


class HelpDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Help")
        self.setWindowIcon(QIcon('imgs/help.ico'))
        contents = ("1.  Use the Drop-down menus, select the resources/location needed." + "\n"
        "2.  Enter the amount of resources you have/want to recycle." + "\n"
        "3.  Click Calculate and view what you got from recycling!")
        self.setText(contents)


class BugReport(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bug Report")
        self.setWindowIcon(QIcon('imgs/bug_report.ico'))
        self.setGeometry(300, 300, 400, 100)

        master = QWidget(self)
        self.setCentralWidget(master)
        layout = QFormLayout(master)


        self.user = QLineEdit(self)
        self.user.setPlaceholderText("Username")

        self.email = QLineEdit(self)
        self.email.setPlaceholderText("Email")

        self.message = QLineEdit(self)
        self.message.setPlaceholderText("Message")

        self.submit = QPushButton(self)
        self.submit.setText("Send Report")

        layout.addRow("Username: ", self.user)
        layout.addRow("Email:", self.email)
        layout.addRow("Message: ", self.message)
        layout.addRow(self.submit)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())