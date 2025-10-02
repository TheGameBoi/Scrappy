from PyQt6.QtWidgets import (QComboBox, QMessageBox, QPushButton, QLabel, QLineEdit, QGridLayout, QApplication,
                             QMainWindow, QGridLayout, QWidget, QTableWidget, QToolBar, QTextEdit, QStatusBar,
                             QTableWidgetItem, QDialog, QPlainTextEdit, QVBoxLayout, QSizePolicy, QHBoxLayout)
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt, QSize
import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scrappy")
        self.setGeometry(300, 300, 200, 100)

        # Layout and Widgets
        widget = QWidget(self)
        layout = QVBoxLayout(widget)

        button = QPushButton("Click Me!")


        layout.addWidget(button)
        self.setCentralWidget(widget)






app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())