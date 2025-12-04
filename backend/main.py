import json
import sys
from pathlib import Path
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import (QComboBox, QMessageBox, QPushButton, QApplication,
                             QMainWindow, QGridLayout, QWidget, QTextEdit, QStatusBar,
                             QSpinBox, QCheckBox, QLabel, QVBoxLayout, QHBoxLayout, QDialog)




main_dir = Path(__file__).parent.resolve()
img_dir = main_dir / "imgs"
json_path = main_dir / "jsons" / "items.json"
css_path = main_dir / "themes" / "mode.css"
icon_file = ["recycler.ico", "help.ico", "info.ico"]
icon_path = {name: img_dir / name for name in icon_file}

try:
    with open(css_path, "r") as style:
                dark_style = style.read()
except FileNotFoundError:
    print("File not found.")
    dark_style = ""


def load_from_json(file_path):
    with open(file_path, 'r') as my_json:
        data = json.load(my_json)
        return data



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scrappy")
        self.setWindowIcon(QIcon(str(icon_path["recycler.ico"])))
        self.setGeometry(300, 300, 680, 280)

        self.theme = 0

        if not json_path.exists():
            print(f"File not found at {json_path}.")
            return

        self.items = load_from_json(json_path)

        master = QWidget(self)
        self.setCentralWidget(master)
        layout = QGridLayout(master)

        self.setStatusBar(QStatusBar(master))
        self.menuBar()

        self.file_menu = self.menuBar().addMenu("&File")

        self.file_help = QAction("&Help", self)
        self.file_menu.addAction(self.file_help)
        self.file_help.triggered.connect(self.help)

        self.file_setting = QAction("&Settings", self)
        self.file_menu.addAction(self.file_setting)
        self.file_setting.triggered.connect(self.setting)

        self.file_about = QAction("&About", self)
        self.file_menu.addAction(self.file_about)
        self.file_about.triggered.connect(self.about)


        self.about_action = QAction("About", self)
        self.setting_action = QAction("&Settings", self)
        self.file_menu.addAction(self.file_about)
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

        self.check = QCheckBox(self)
        self.check.setText("Dark Theme")
        self.check.clicked.connect(self.toggle_themes)


        # Add widgets to the layout
        layout.addWidget(self.check, 4, 0, 2, 2)
        layout.addWidget(self.result, 0, 0, 1, 2)
        layout.addWidget(self.group, 2, 0)
        layout.addWidget(self.list, 2, 1)
        layout.addWidget(self.choice, 3, 0)
        layout.addWidget(self.amount, 3, 1)
        layout.addWidget(self.calculate, 4, 0, 1, 2)


    def toggle_themes(self):
        self.theme = 0 if self.theme == 1 else 1
        if self.theme == 1:
            if dark_style:
                self.setStyleSheet(dark_style)
        else:
            self.setStyleSheet("")


    def about(self):
        self.about_dialog = AboutDialog(self)
        self.about_dialog.show()


    def help(self):
        self.help_dialog = HelpDialog(self)
        self.help_dialog.show()


    def setting(self):
        self.setting_dialog = SettingDialog(self)
        self.setting_dialog.show()


    def grouping(self):
        self.group.clear()
        for group in self.items['Items']:
            self.group.addItem(group)


    def listing(self):
        self.list.clear()
        selected_group = self.group.currentText()
        if selected_group in self.items['Items']:
            group_items = self.items['Items'][selected_group]
            for resource in group_items:
                self.list.addItem(resource)


    def calculator(self):
        resource = self.list.currentText()
        amount = self.amount.value()
        location = self.choice.currentText()

        selected_group = self.group.currentText()
        group_data = self.items['Items'].get(selected_group, {})
        res = group_data.get(resource)

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



class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About Us")
        self.setGeometry(300, 300, 300, 100)
        self.setWindowIcon(QIcon(str(icon_path["info.ico"])))

        layout = QGridLayout(self)
        self.setLayout(layout)

        self.about = QLabel(self)
        self.about.setText(
        "        Scrappy Version 0.1" + "\n"
        "        Made by TheGameBoi" + "\n"
        "        All rights and copyrights reserved"
        )

        layout.addWidget(self.about, 0, 0)


class HelpDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Help")
        self.setGeometry(300, 300, 400, 100)
        self.setWindowIcon(QIcon(str(icon_path["help.ico"])))

        layout = QGridLayout(self)
        self.setLayout(layout)

        self.guides = QLabel(self)
        self.guides.setText(
        "How to use Scrappy:" + "\n" + "\n"
        "       1. Select a type of resource from the dropdown box. (Components, etc)" + "\n"
        "       2. Choose the item you are going to recycle. (Tech Trash, Electric Fuse, etc)" + "\n"
        "       3. Select a location to recycle from. (Safe-Zone/Monument)" + "\n"
        "       4. Enter the number of your resources into the number box. (0-500)" + "\n"
        "       5. Click the Calculate button and see what you got from recycling!"
        )

        layout.addWidget(self.guides, 0, 0)


class SettingDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setGeometry(300, 300, 300, 100)
        self.setWindowIcon(QIcon(str(icon_path["info.ico"])))

        layout = QGridLayout(self)
        self.setLayout(layout)




app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())