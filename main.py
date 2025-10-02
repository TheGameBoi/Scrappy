from PyQt6.QtWidgets import (QComboBox, QMessageBox, QPushButton, QLabel, QLineEdit, QGridLayout, QApplication,
     QMainWindow, QGridLayout, QWidget, QTableWidget, QToolBar, QTextEdit, QStatusBar,
     QTableWidgetItem, QDialog, QPlainTextEdit, QVBoxLayout)
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt
import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scrappy")
        self.setGeometry(300, 300, 400, 400)





app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()