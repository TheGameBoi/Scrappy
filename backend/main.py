import sys
from PyQt6.QtCore import QEvent
from PyQt6.QtGui import QIcon, QAction
from progression import ProgressionManager
from menu_dialogs import AboutDialog, HelpDialog
from recycle_logger import RecycleLogManager
from directories import icon_path, load_from_json, items
from PyQt6.QtWidgets import (QComboBox, QPushButton, QApplication,
                             QMainWindow, QGridLayout, QWidget, QTextEdit, QStatusBar,
                             QSpinBox, QLabel)



class MainWindow(QMainWindow):
    def __init__(self, my_app, parent=None):
        super().__init__(parent)
        self.app = my_app
        self.setWindowTitle("Scrappy")
        self.setWindowIcon(QIcon(str(icon_path["scrappy.ico"])))
        self.setGeometry(300, 300, 680, 280)
        self.is_dark_mode = False # Keeps track of the current theme.

        self.progression = ProgressionManager()
        self.recycle_logger = RecycleLogManager()

        # Error handling for JSON data.
        if not items.exists():
            print(f"File not found at {items}.")
            return

        # Items list for JSON.
        self.items = load_from_json(items)

        # MainWindow widgets and File Menu actions.
        master = QWidget(self)
        self.setCentralWidget(master)
        layout = QGridLayout(master)

        self.setStatusBar(QStatusBar(master))
        self.menuBar()

        self.file_menu = self.menuBar().addMenu("&File")

        self.file_help = QAction("&Help", self)
        self.file_menu.addAction(self.file_help)
        self.file_help.triggered.connect(self.help)


        self.file_about = QAction("&About", self)
        self.file_menu.addAction(self.file_about)
        self.file_about.triggered.connect(self.about)


        self.about_action = QAction("About", self)
        self.setting_action = QAction("&Settings", self)
        self.file_menu.addAction(self.file_about)
        self.about_action.triggered.connect(self.about)


        self.twitter = QLabel(
            f'<a href="https://x.com/ImGameBoi"><img src="{str(icon_path["x.png"])}" width="16" height="16"></a>', self)
        self.twitter.setOpenExternalLinks(True)
        self.statusBar().addPermanentWidget(self.twitter)

        self.github = QLabel(
            f'<a href="https://github.com/TheGameBoi/Scrappy"><img src="{str(icon_path["github.png"])}" width="16" height="16"></a>', self)
        self.github.setOpenExternalLinks(True)
        self.statusBar().addPermanentWidget(self.github)

        # QComboBoxes
        self.amount = QSpinBox(self)
        self.amount.setRange(0, 500)

        self.choice = QComboBox(self)
        self.choice.addItem("Safe-Zone")
        self.choice.addItem("Monument")

        self.group = QComboBox(self)
        self.group.setFixedWidth(200)
        self.group.currentIndexChanged.connect(self.listing)

        self.list = QComboBox(self)
        self.list.setFixedWidth(200)

        # Loads the QComboBox lists.
        self.grouping()
        self.listing()

        # Buttons and Labels
        self.calculate = QPushButton("Calculate", self)
        self.calculate.clicked.connect(self.calculator)

        self.result = QTextEdit(self)
        self.result.setReadOnly(True)
        self.result.setFixedHeight(70)

        # Add widgets to the layout
        layout.addWidget(self.result, 0, 0, 1, 2)
        layout.addWidget(self.group, 2, 0)
        layout.addWidget(self.list, 2, 1)
        layout.addWidget(self.choice, 3, 0)
        layout.addWidget(self.amount, 3, 1)
        layout.addWidget(self.calculate, 4, 0, 1, 2)


    def about(self):
        self.about_dialog = AboutDialog(self)
        self.about_dialog.show()


    def help(self):
        self.help_dialog = HelpDialog(self)
        self.help_dialog.show()


    def grouping(self):
        self.group.clear()
        # Selects the Items list and searches for each group type.
        for group in self.items['Items']:
            self.group.addItem(group)


    def listing(self):
        self.list.clear()
        # Searches through the selected_group data for resources.
        selected_group = self.group.currentText()
        if selected_group in self.items['Items']:
            group_items = self.items['Items'][selected_group]
            for resource in group_items:
                self.list.addItem(resource)

    # Calculate Function.
    def calculator(self):
        resource = self.list.currentText()
        amount = self.amount.value()
        location = self.choice.currentText()

        selected_group = self.group.currentText()
        group_data = self.items['Items'].get(selected_group, {})
        res = group_data.get(resource)

        # For loop that parses JSON data as a dictionary and calculates the data correctly.
        my_dict = {}
        for key, value in res.items():
            if location == 'Safe-Zone':
                my_dict[key] = value * amount * 0.8
            if location == 'Monument':
                my_dict[key] = value * amount * 1.2

        self.recycle_logger.add_entry(
            item_name=resource,
            quantity=amount,
            location=location,
            results=my_dict
        )

        # Gets the total scrap, and then saves it to the JSON file.
        total_scrap = self.recycle_logger.total_earned_scrap()
        self.progression.total_earned_scrap = total_scrap
        self.progression.save_progression()

        # Join method that joins the calculated results together.
        split = ', '.join(f"{int(v)} {k}" for k, v in my_dict.items())
        new_split = [f"{int(v)} {k}" for k, v in my_dict.items()]
        new_var = ""

        # Displays the results to the QLabel widget.
        for i, v in enumerate(new_split):
            if i == len(new_split) - 1:
                new_var += f'and {v}'
            else:
                new_var += f'{v}, '
        self.result.setText(f"Recycling {amount} {resource} at {location} will give you {new_var}.")
        self.statusBar().showMessage(f"Total Scrap Recycled: {int(total_scrap)}", 5000)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(app)
    window.show()
    sys.exit(app.exec())