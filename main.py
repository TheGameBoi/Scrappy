from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon, QAction
from PyQt6.QtWidgets import (QComboBox, QMessageBox, QPushButton, QLabel, QLineEdit, QGridLayout, QApplication,
                             QMainWindow, QGridLayout, QWidget, QTableWidget, QToolBar, QTextEdit, QStatusBar,
                             QTableWidgetItem, QDialog, QPlainTextEdit, QVBoxLayout, QSizePolicy, QHBoxLayout,
                             QStyleFactory, QFormLayout, QSpinBox, QListWidget)
import sys
import items
from items import dark_mode_stylesheet
import json


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scrappy")
        self.setGeometry(300, 300, 700, 300)
        self.setStyleSheet(dark_mode_stylesheet())


        master = QWidget(self)
        self.setCentralWidget(master)
        layout = QFormLayout(master)


        self.amount = QSpinBox(self)
        self.amount.setRange(0, 500)


        self.group = QComboBox(self)


        self.choice = QComboBox(self)
        self.choice.addItem("Safe-Zone")
        self.choice.addItem("Monument")


        self.calculate = QPushButton("Calculate", self)

        self.result = QLabel(self)


        # Add widgets to the layout with labels
        layout.addRow("Item:", self.group)
        layout.addRow("Amount:", self.amount)
        layout.addRow("Location:", self.choice)
        layout.addRow(self.calculate)
        layout.addRow("Result:", self.result)


        # Add some spacing and padding
        layout.setVerticalSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())