from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import (QComboBox, QMessageBox, QPushButton, QLabel, QLineEdit, QGridLayout, QApplication,
        QMainWindow, QGridLayout, QWidget, QTableWidget, QToolBar, QTextEdit, QStatusBar,
        QTableWidgetItem, QDialog, QPlainTextEdit, QVBoxLayout, QSizePolicy, QHBoxLayout,
        QStyleFactory)
import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scrappy")
        self.setGeometry(300, 300, 900, 300)


        # Labels, Buttons, etc...
        label_one = QLabel("1")
        label_two = QLabel("2")
        label_three = QLabel("3")

        button_one = QPushButton("Button One")
        button_two = QPushButton("Button Two")
        button_three = QPushButton("Button Three")


        # Master Layout and Rows
        master = QVBoxLayout()

        row_one = QHBoxLayout()
        row_two = QHBoxLayout()
        row_three = QHBoxLayout()


        # Main Display
        row_one.addWidget(label_one, alignment=Qt.AlignmentFlag.AlignLeft)
        row_one.addWidget(label_two, alignment=Qt.AlignmentFlag.AlignLeft)
        row_one.addWidget(label_three, alignment=Qt.AlignmentFlag.AlignCenter)
        row_two.addWidget(button_one, alignment=Qt.AlignmentFlag.AlignCenter)
        row_two.addWidget(button_two, alignment=Qt.AlignmentFlag.AlignCenter)
        row_two.addWidget(button_three, alignment=Qt.AlignmentFlag.AlignCenter)

        master.addLayout(row_one)
        master.addLayout(row_two)
        master.addLayout(row_three)

        widget = QWidget(self)
        widget.setLayout(master)
        self.setCentralWidget(widget)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())