from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon
from directories import icon_path
from PyQt6.QtWidgets import QGridLayout, QLabel, QDialog, QCheckBox, QWidget, QVBoxLayout


class HelpDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Help")
        self.setGeometry(300, 300, 400, 100)
        self.setWindowIcon(QIcon(str(icon_path["help.ico"])))

        layout = QGridLayout(self)
        self.setLayout(layout)

        # QLabel widget that displays help info.
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
    theme_change = pyqtSignal(bool)
    def __init__(self, initial_dark_mode=False, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setGeometry(300, 300, 300, 100)
        self.setWindowIcon(QIcon(str(icon_path["info.ico"])))

        # Dialog Modal blocks interaction with Main Window
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        # Master layout
        master = QWidget(self)
        layout = QVBoxLayout(master)
        self.setLayout(layout)

        self.dark_box = QCheckBox(self)
        self.dark_box.setText("Enable Dark Theme")
        # Initial state, which is false, won't fire automatically
        self.dark_box.setChecked(initial_dark_mode)
        # Connect the Checkbox to emit a signal
        self.dark_box.stateChanged.connect(self.toggle_themes)

        layout.addWidget(self.dark_box)

    def toggle_themes(self, state):
        """
        This slot is called when the checkbox state changes.
        It emits our custom signal with the new theme state.
        """
        # The Checkbox state is an integer, default of 0, Active of 2.
        is_dark = (state == 2)
        # Emits the signal
        self.theme_change.emit(is_dark)



class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About Us")
        self.setGeometry(300, 300, 300, 100)
        self.setWindowIcon(QIcon(str(icon_path["info.ico"])))

        layout = QGridLayout(self)
        self.setLayout(layout)

        # QLabel widget that displays about info.
        self.about = QLabel(self)
        self.about.setText(
        "        Scrappy Version 0.1" + "\n"
        "        Made by TheGameBoi" + "\n"
        "        All rights and copyrights reserved"
        )

        layout.addWidget(self.about, 0, 0)