from PyQt6.QtGui import QIcon
from directories import icon_path
from PyQt6.QtWidgets import QGridLayout, QLabel, QDialog, QWidget, QDialogButtonBox


class HelpDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Help")
        self.setGeometry(300, 300, 400, 100)
        self.setWindowIcon(QIcon(str(icon_path["help.ico"])))

        master = QWidget(self)
        layout = QGridLayout(master)
        self.setLayout(layout)

        # QLabel widget that displays help info.
        self.guides = QLabel(self)
        self.guides.setText(
        "How to use Scrappy:" + "\n" + "\n"
        "1. Select a type of resource from the dropdown box. (Components, etc)" + "\n"
        "2. Choose the item you are going to recycle. (Tech Trash, Electric Fuse, etc)" + "\n"
        "3. Select a location to recycle from. (Safe-Zone/Monument)" + "\n"
        "4. Enter the number of your resources into the number box. (0-500)" + "\n"
        "5. Click the Calculate button and see what you got from recycling!"
        )
        self.guides.setWordWrap(True)

        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        layout.addWidget(self.guides)
        layout.addWidget(self.button_box)


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About Us")
        self.setGeometry(300, 300, 300, 100)
        self.setWindowIcon(QIcon(str(icon_path["info.ico"])))

        master = QWidget(self)
        layout = QGridLayout(master)
        self.setLayout(layout)

        # QLabel widget that displays about info.
        self.about = QLabel(self)
        self.about.setText(
        "        Scrappy Version 0.3" + "\n"
        "        Made by TheGameBoi" + "\n"
        "        All Rights and Copyrights Reserved 2026."
        )

        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        layout.addWidget(self.about)
        layout.addWidget(self.button_box)